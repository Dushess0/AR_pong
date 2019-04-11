import pygame
import json
from settings import *
from pygame.locals import *
from game_classes import *
import cv2


def game_loop(screen, template1, template2, CLOCK):
    try:
        with open(calibration_FILE, 'r') as f:
            calib_data = json.load(f)
    except FileNotFoundError:
        pass

   
    player_1 = Pad(number=1,
                   scale=calib_data[0]['scale'],
                   threshold=calib_data[0]['threshold'],
                   delta=calib_data[0]['delta']
                   )
    player_2 = Pad(number=2,
                   scale=calib_data[1]['scale'],
                   threshold=calib_data[1]['threshold'],
                   delta=calib_data[1]['delta']
                   )
    ball = Ball()
   
    capture = cv2.VideoCapture(0)
    ret, frame = capture.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    x, camera_res = img_gray.shape[::-1]
    del x, img_gray, image
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == KEYDOWN:

                if event.key == K_RETURN:
                    player_1.pos[1] += 10
                if event.key == K_i:
                    player_1.pos[1] -= 10
                if event.key == K_ESCAPE:
                    running = False

        ret, frame = capture.read()

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        player_1.move(img_gray, template1, camera_res)
        player_2.move(img_gray, template2, camera_res)
        player_1.draw(screen)
        player_2.draw(screen)
        ball.move(1 / FPS, player_1, player_2)
        ball.update(screen)

        pygame.display.update()

        CLOCK.tick(FPS)

    screen.blit(MENU_OPTIONS,(0,0))