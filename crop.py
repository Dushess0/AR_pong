import numpy as np
import cv2
import time
import random
import datetime


# cv2.createTrackbar("AR Pong" , value, count, onChange)
#сalibration
#show model . model continuosky updating in crop function
def calibrate ( refPt ):
    global model , resp
    while True:
        cv2.imshow("frame", model )
        key = cv2.waitKey(1) & 0xFF
        if key == ord("c"):
            break
    try:
        refPt[0] = list(refPt[0])
        refPt[1] = list(refPt[1])
        if refPt[0][1] > refPt[1][1]:
            refPt[0][1], refPt[1][1] = refPt[1][1], refPt[0][0]
        if refPt[0][0] > refPt[1][0]:
            refPt[0][0], refPt[1][0] = refPt[1][0], refPt[0][0]

        cropped = model[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
        gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", gray)
        resp = cv2.waitKey(0)
        cv2.imwrite("models/" + str(datetime.datetime.now()) + ".jpg", gray)
        return gray
    except :
        return []


#draw rectangle and grop the image
def crop(event, x, y, flags, params):
    global refPt, cropping , model , clone
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(refPt) == 2:
            model = clone.copy()
            refPt.clear()

        refPt.append((x, y))
        cropping = True
    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cv2.rectangle(model, refPt[0], (x, y), (0, 255, 125), 2)
        cropping = False

#end


def make_a_sample():
    global model , refPt , clone , cropping , resp
    capture=cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1500)
    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("frame", crop)

    while 2+2!=5:

        ret, frame = capture.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        image = cv2.flip(image, 3)
        cv2.imshow('frame', image)
        key = cv2.waitKey(20)
        print(key)
        if key == ord('c'):
                refPt = []

                cropping = False
                # running = True
                model = cv2.flip(capture.read()[1], 3)
                clone = model.copy()
                calibrate(refPt)
                if resp == ord('c'):
                    return
        elif key == ord('e'):
            capture.release()
            cv2.destroyAllWindows()
            return


    capture.release()
    cv2.destroyAllWindows()