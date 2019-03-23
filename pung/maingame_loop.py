
import pygame
from settings import *
from pygame.locals import *
from game_classes import *
import cv2




def game_loop(template1, template2):
    player_1 = Pad(1)
    player_2 = Pad(2)
    ball = Ball()
    capture = cv2.VideoCapture(0)
    ret, frame = capture.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    x, sensity = img_gray.shape[::-1]
    del x, img_gray, image
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:

                if event.key == K_RETURN:
                    player_1.pos[1] += 10
                if event.key == K_i:
                    player_1.pos[1] -= 10

        ret, frame = capture.read()

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        player_1.move(img_gray, template1, 0.5, sensity)
        player_2.move(img_gray, template2, 0.5, sensity)
        player_1.draw(screen)
        player_2.draw(screen)
        ball.move(1 / FPS, player_1, player_2)
        ball.update(screen)

        pygame.display.update()

        CLOCK.tick(FPS)
