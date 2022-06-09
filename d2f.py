import cv2
import os
import sys
from detect_face import detect_face

def get_roi(filename):
    image = cv2.imread(filename)
    roi = image[0:62, 1840:1920]
    return roi

def get_hist(image):
    cv2.normalize(image, image, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    return cv2.calcHist([image], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])

def main():
    try:
        ignore = open("ignore.txt").read().splitlines()
    except:
        ignore = []

    streamer, viewers = sys.argv[1].split('#')

    if streamer in ignore:
        return

    if os.system(f"./scripts/get_twitch_frame {streamer}") != 0:
        return

    quit_button = cv2.imread("quit_button.jpg")
    roi = get_roi(f"frames/{streamer}.jpg")
    #cv2.imwrite(f"frames/{streamer}.jpg", roi)
    compare = cv2.compareHist(get_hist(quit_button), get_hist(roi), cv2.HISTCMP_BHATTACHARYYA) * 100
    if compare <= 10:
        face_detected = detect_face(f"frames/{streamer}.jpg")
        print(f"https://twitch.tv/{streamer} (confidence: {compare}, viewers: {viewers}, faces detected: {face_detected})")

if __name__ == "__main__":
    main()
