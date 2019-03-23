import pygame

from settings import *
from Button_Classes import Button
import image_choosing
import maingame_loop
import cv2
import numpy

pygame.font.init()
MENU_OPTIONS = pygame.image.load('data/menu/OPTIONS_MAIN.jpg')
COLOR = (0 ,125 , 200)
FONT = pygame.font.Font("data/Anurati-Regular.otf", 85)
LEFT_CALLIBRATE_BUTTON = [0.05 * WINDOWS_WIDTH , 0.8 * WINDOWS_HEIGHT ]
RIGHT_CALLIBRATE_BUTTON = [0.75 * WINDOWS_WIDTH , 0.8 * WINDOWS_HEIGHT ]
PLAY_BUTTON = [0.3 * WINDOWS_WIDTH , 0.1 * WINDOWS_HEIGHT]
PLAYER_ONE_IMAGE = ((0.05 * WINDOWS_WIDTH , 0.1 * WINDOWS_HEIGHT , 0.2 * WINDOWS_WIDTH , 0.6 * WINDOWS_HEIGHT) )
PLAYER_TWO_IMAGE = ((0.75 * WINDOWS_WIDTH , 0.1 * WINDOWS_HEIGHT , 0.2 * WINDOWS_WIDTH , 0.6 * WINDOWS_HEIGHT) )


def call_game(template):
    template1 = cv2.imread(template[0], 0)
    template2 = cv2.imread(template[1], 0)

    pygame_version.game_loop(template1, template2)

def main(screen ,template1 , template2 , im1 , im2):
    screen.blit(MENU_OPTIONS, (0,0))
    while True:
        play = Button(0.2 * WINDOWS_WIDTH ,0.05 * WINDOWS_HEIGHT , PLAY_BUTTON , "Play" )
        l_call_btn = Button(0.1 * WINDOWS_WIDTH ,0.05 * WINDOWS_HEIGHT , LEFT_CALLIBRATE_BUTTON , "Callibrate player one"  )
        r_call_btn = Button(0.1 * WINDOWS_WIDTH ,0.05 * WINDOWS_HEIGHT , RIGHT_CALLIBRATE_BUTTON , "Callibrate player one"  )
        screen.blit(im1,(0.05 * WINDOWS_WIDTH , 0.1 * WINDOWS_HEIGHT))
        screen.blit(im2,(0.75 * WINDOWS_WIDTH , 0.1 * WINDOWS_HEIGHT))
        play.draw(screen)
        r_call_btn.draw(screen)
        l_call_btn.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                play.react_on_click(call_game , (template1 , template2))
                l_call_btn.react_on_click()
                r_call_btn.react_on_click()
        pygame.draw.rect(screen,COLOR,PLAYER_ONE_IMAGE,2)
        pygame.draw.rect(screen,COLOR,PLAYER_TWO_IMAGE,2)

        pygame.display.update()






