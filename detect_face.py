import numpy as np
import cv2
import time
import sys

def show_image(img):
    cv2.imshow('Test Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def get_faces(img):
    #lbp_face_cascade = cv2.CascadeClassifier('../Face-Detection-OpenCV/data/lbpcascade_frontalface.xml')
    haar_face_cascade = cv2.CascadeClassifier('../Face-Detection-OpenCV/data/haarcascade_frontalface_alt.xml')
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #show_image(gray_img)
    return haar_face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

def detect_face(filename):
    img = cv2.imread(filename)

    num_faces = 0
    for dimensions in [[280, 800, 0, 570], [280, 800, 1350, 570]]:
        roi = img[
            dimensions[0]:dimensions[0]+dimensions[1],
            dimensions[2]:dimensions[2]+dimensions[3]
        ].copy()
        faces = get_faces(roi)
        for (x, y, w, h) in faces:
            num_faces += 1
            cv2.rectangle(
                img,
                (x+dimensions[2], y+dimensions[0]),
                (x+w+dimensions[2], y+h+dimensions[0]),
                (0, 255, 0),
                2
            )
    cv2.imwrite(filename, img)

    return num_faces

if __name__ == "__main__":
    print(detect_face(sys.argv[1]))
