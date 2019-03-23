import numpy as np
import cv2
import time
import random
import datetime
import pygame
from pygame.locals import *

refPt = []


# cv2.createTrackbar("AR Pong" , value, count, onChange)
# сalibration
# show model . model continuosky updating in crop function
def calibrate(refPt):
    global model, resp
    while True:
        cv2.imshow("frame", model)
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
        if resp == ord('c'):
            cv2.imwrite(SAMPLES_FOLDER + str(datetime.datetime.now()) + ".jpg", gray)
            return gray
        else:
            return []
    except:
        return []


# draw rectangle and grop the image
def crop(event, x, y, flags, params):
    global refPt, cropping, model, clone
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


# end


def make_a_sample(screen):
    global model, clone, cropping, resp
    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1500)
    # cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    # cv2.setMouseCallback("frame", crop)

    camera_on = True
    run = True
    ready_to_crop = False
    camera_pos_x = 200
    camera_pos_y = 400
    while run:

        if camera_on:
            frame = capture.read()[1]
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = cv2.flip(image, 3)
            current_image = pygame.image.frombuffer(image.tostring(), image.shape[1::-1], "RGB")

        # cv2.imshow('frame', image)
        # key = cv2.waitKey(20)
        # print(key)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                if event.key == K_RETURN:
                    if camera_on:
                        camera_on = False
                        model = cv2.flip(capture.read()[1], 3)
                        model = cv2.cvtColor(model, cv2.COLOR_BGR2RGB)
                        current_image = pygame.image.frombuffer(model.tostring(), model.shape[1::-1], "RGB")
                    if ready_to_crop:
                        # current_image = pygame.image.frombuffer(model.tostring(), model.shape[1::-1], "RGB")
                        cv2.imwrite(SAMPLES_FOLDER + str(datetime.datetime.now()) + ".jpg", final)
                        return final

            if event.type == MOUSEBUTTONDOWN and not camera_on:
                if event.button == 1:
                    refPt.append([event.pos[0] - camera_pos_x, event.pos[1] - camera_pos_y])

        if len(refPt) == 2:
            print(refPt)
            if refPt[0][1] > refPt[1][1]:
                refPt[0][1], refPt[1][1] = refPt[1][1], refPt[0][1]
            if refPt[0][0] > refPt[1][0]:
                refPt[0][0], refPt[1][0] = refPt[1][0], refPt[0][0]

            result = model[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
            final = result.copy()

            cv2.rectangle(model, tuple(refPt[0]), tuple(refPt[1]), (0, 255, 125), 2)
            current_image = pygame.image.frombuffer(model.tostring(), model.shape[1::-1], "RGB")
            ready_to_crop = True
            refPt.append(0)

        screen.blit(current_image, (camera_pos_x, camera_pos_y))

        pygame.display.update()

        # if key == ord('c'):
        #     refPt = []
        #
        #     cropping = False
        #     # running = True
        #     model = cv2.flip(capture.read()[1], 3)
        #     clone = model.copy()
        #     calibrate(refPt)
        #     # if not c repeat loop utnlie success
        #     if resp == ord('c'):
        #         capture.release()
        #         cv2.destroyAllWindows()
        #         return
        # elif key == ord('e'):
        #     capture.release()
        #     cv2.destroyAllWindows()
        #     return

    capture.release()
    cv2.destroyAllWindows()
