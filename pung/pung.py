import numpy as np
import cv2
from settings import *
import time
import random
import math
import statistics


def draw_pad(image, pos, player="green"):
    if player == "green":
        color = (0, 255, 0)
    else:
        color = (255, 0, 0)
    cv2.rectangle(image, (int(pos[0] - PAD_WIDTH), int(pos[1] - PAD_HEIGHT)),
                  (int(pos[0] + PAD_WIDTH), int(pos[1] + PAD_HEIGHT)), color, -1)


def draw_ball(image, pos):
    cv2.circle(image, (int(pos[0]), int(pos[1])), BALL_RADIUS, (0, 0, 255), -1)


class Pad:
    def __init__(self, number):
        self.score = 0
        if number == 1:
            self.pos = [PAD_WIDTH * 4, WINDOWS_HEIGHT / 2]

        elif number == 2:
            self.pos = [WINDOWS_WIDTH - PAD_WIDTH, WINDOWS_HEIGHT / 2]
        self.number = number
        self.speed = 50

    def move_up(self):
        self.pos[1] -= self.speed

    def move_down(self):
        self.pos[1] += self.speed


class Ball:
    def __init__(self):

        self.pos = [600, 450]
        self.speed = BALL_SPEED
        self.generate_angle()
        self.acceleration = BALL_ACCELERATION

    def move(self, dt, pad1, pad2):
        pass
        # self.pos[0]+=dt*self.speed*math.cos(self.angle)
        # self.pos[1]-=dt*self.speed*math.sin(self.angle)
        # self.collide(pad1,pad2)

    def generate_angle(self):
        while 1:
            divider = 6
            self.angle = 2 * math.pi * random.random()
            if self.angle > math.pi * 2 - math.pi / divider and self.angle < math.pi / divider:

                if self.angle > math.pi / 2 - math.pi / divider and self.angle < math.pi / 2 + math.pi / divider:

                    if self.angle > math.pi - math.pi / divider and self.angle < math.pi + math.pi / divider:

                        if self.angle > math.pi * 3 / 2 - math.pi / divider and self.angle < math.pi * 3 / 2 + math.pi / divider:
                            continue

            break

    def respawn(self, winner):
        self.generate_angle()
        self.speed = BALL_SPEED
        self.pos = [300, 300]
        winner.score += 1

    def collide(self, pad1, pad2):

        if self.pos[0] + BALL_RADIUS > pad2.pos[0] - PAD_WIDTH / 2:
            if self.pos[1] < pad2.pos[1] + PAD_HEIGHT / 2 + BALL_RADIUS and self.pos[1] > pad2.pos[
                1] - PAD_HEIGHT / 2 - BALL_RADIUS:
                self.angle = math.pi - self.angle
                self.speed += self.acceleration

        if self.pos[0] - BALL_RADIUS < pad1.pos[0] + PAD_WIDTH / 2:
            if self.pos[1] < pad1.pos[1] + PAD_HEIGHT / 2 + BALL_RADIUS and self.pos[1] > pad1.pos[
                1] - PAD_HEIGHT / 2 - BALL_RADIUS:
                self.angle = math.pi - self.angle
                self.speed += self.acceleration

        if self.pos[1] < BALL_RADIUS:
            self.angle = math.pi * 2 - self.angle
        if self.pos[1] > 500 - BALL_RADIUS:
            self.angle = math.pi * 2 - self.angle
        if self.pos[0] > 650:
            self.respawn(pad1)
        if self.pos[0] < -50:
            self.respawn(pad2)


def find_template(where, picture, pad, threshold=0.3, color=(0, 0, 255)):
    img_gray = cv2.cvtColor(where, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(img_gray, picture, cv2.TM_CCOEFF_NORMED)
    w, h = picture.shape[::-1]

    loc = np.where(res >= threshold)
    print(loc)
    X = []
    Y = []
    for pt in zip(*loc[::-1]):
        X.append(pt[0])
        Y.append(pt[1])
    if X == []:
        return
    mean_x = int(statistics.median(X))
    mean_y = int(statistics.median(Y))

    pad.pos = [(2 * mean_x + h) / 2, (2 * mean_y + h) / 2]


def main():
    capture = cv2.VideoCapture(0)
    capture.set(4, WINDOWS_HEIGHT)
    capture.set(3, WINDOWS_WIDTH)
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', WINDOWS_WIDTH, WINDOWS_HEIGHT)
    player_1 = Pad(1)
    player_2 = Pad(2)
    ball = Ball()
    font = cv2.FONT_HERSHEY_SIMPLEX
    template1 = cv2.imread('green.jpg', 0)

    template2 = cv2.imread('blue.jpg', 0)

    while 2 + 2 != 5:
        ret, frame = capture.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

        draw_pad(image, player_1.pos)
        draw_pad(image, player_2.pos, "blue")
        draw_ball(image, ball.pos)
        cv2.putText(image, str(player_1.score) + "  :  " + str(player_2.score), (250, 100), font, 1, (19, 19, 118), 5,
                    cv2.LINE_AA)
        cv2.imshow('frame', image)
        key = cv2.waitKey(20)
        find_template(image, template1, player_1, threshold=0.6)

        image = cv2.flip(image, 3)

        ball.move(1 / 60, player_1, player_2)
        time.sleep(1 / 60)

    capture.release()
    cv2.destroyAllWindows()
