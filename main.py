"""
query {
  game(name: "Dota 2") {
    streams(first: 30, after: null) {
      edges {
        cursor
        node {
          viewersCount
          broadcaster {
            displayName
          }
        }
      }
    }
  }
}
"""

import cv2
import os
import sys

def get_roi(filename):
    image = cv2.imread(filename)
    roi = image[0:62, 1840:1920]
    return roi

def get_hist(image):
    cv2.normalize(image, image, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    return cv2.calcHist([image], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])

def main():
    streamer = sys.argv[1];
    if (os.system(f"./get_twitch_frame {streamer}") != 0):
        print("Could not get twitch frame.")
        return

    quit_button = cv2.imread("quit_button.jpg")
    roi = get_roi(f"frames/{streamer}.jpg")
    cv2.imwrite(f"frames/{streamer}.jpg", roi)
    compare = cv2.compareHist(get_hist(quit_button), get_hist(roi), cv2.HISTCMP_BHATTACHARYYA) * 100
    print(f"Confidence: {compare}")
    if compare <= 10:
        print("User is in main menu")

if __name__ == "__main__":
    main()
