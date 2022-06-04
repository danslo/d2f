import numpy as np
import cv2
import time
import sys

def show_image(img):
    cv2.imshow('Test Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def get_faces(img):
    cascades = {
       "haar_frontal": cv2.CascadeClassifier('../opencv/data/haarcascades/haarcascade_frontalface_default.xml'),
       "haar_profile": cv2.CascadeClassifier('../opencv/data/haarcascades/haarcascade_profileface.xml'),
       "lbp_profile": cv2.CascadeClassifier('../opencv/data/lbpcascades/lbpcascade_profileface.xml'),
       "lbp_frontal": cv2.CascadeClassifier('../opencv/data/lbpcascades/lbpcascade_frontalface_improved.xml'),
    }
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = []
    for label, cascade in cascades.items():
        if len(faces): break
        for face in cascade.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=7, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE):
            faces.append(face)
    return faces

def detect_face(filename):
    img = cv2.imread(filename)

    num_faces = 0

    roi_areas = [
        [700, 380, 0, 570],    # bottom left
        [700, 380, 1350, 570], # bottom right
        [0, 700, 0, 330],      # left stroke
        [0, 700, 1590, 330],   # right stroke
    ]
    for dimensions in roi_areas:
        roi = img[
            dimensions[0]:dimensions[0]+dimensions[1],
            dimensions[2]:dimensions[2]+dimensions[3]
        ].copy()
        faces = get_faces(roi)
        num_faces += len(faces)
        for (x, y, w, h) in faces:
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
