import pygame
import json

from settings import *
from Button_Classes import Button
import image_choosing
import maingame_loop
import cv2
import numpy
import callibrating


pygame.font.init()
MENU_OPTIONS = pygame.image.load(OPTIONS_BACKGROUND)
COLOR = (0, 125, 200)
FONT = pygame.font.Font(PLAYER_NUMBER_FONT, 85)

LEFT_CALLIBRATE_BUTTON = [0.05 * WINDOWS_WIDTH, 0.8 * WINDOWS_HEIGHT]
RIGHT_CALLIBRATE_BUTTON = [0.75 * WINDOWS_WIDTH, 0.8 * WINDOWS_HEIGHT]

PLAY_BUTTON = [0.3 * WINDOWS_WIDTH, 0.3 * WINDOWS_HEIGHT]
PLAYER_ONE_IMAGE = ((0.05 * WINDOWS_WIDTH, 0.1 * WINDOWS_HEIGHT, 0.2 * WINDOWS_WIDTH, 0.6 * WINDOWS_HEIGHT))
PLAYER_TWO_IMAGE = ((0.75 * WINDOWS_WIDTH, 0.1 * WINDOWS_HEIGHT, 0.2 * WINDOWS_WIDTH, 0.6 * WINDOWS_HEIGHT))
MENU_BUTTON = [0.45 * WINDOWS_WIDTH, 0.8 * WINDOWS_HEIGHT]


def call_game(argv):
    screen = argv[0]
    clock = argv[1]
    template1_filename = argv[2]
    template2_filename = argv[3]
    template1=cv2.imread(template1_filename,0)
    template2=cv2.imread(template2_filename,0)

    with open(CALLIBRATION_FILE, 'w+') as f:
        json.dump(calib_data, f)

    maingame_loop.game_loop(screen=screen,
                            CLOCK=clock,
                            template1=template1,
                            template2=template2
                            )


def return_to_menu():
    global running
    running = False


def call_callibration(argv):
    screen = argv[0]
    clock = argv[1]
    model = argv[2]
    player = argv[3]
    template=cv2.imread(model,0)
    data = callibrating.player_test(screen, clock, template)
    calib_data[player] = data
    


def main(screen, clock, template1, template2, im1, im2):
    global running , calib_data
    try:
        with open(CALLIBRATION_FILE, 'r') as f:
            calib_data = json.load(f)
    except FileNotFoundError:
        pass
    screen.blit(MENU_OPTIONS, (0, 0))
    running = True
    while running:
        play = Button(0.2 * WINDOWS_WIDTH,
                      0.05 * WINDOWS_HEIGHT,
                      PLAY_BUTTON,
                      "Play",
                      normalize=1)
        l_call_btn = Button(0.1 * WINDOWS_WIDTH,
                            0.05 * WINDOWS_HEIGHT,
                            LEFT_CALLIBRATE_BUTTON,
                            "Callibrate player one",
                            normalize=1)
        r_call_btn = Button(0.1 * WINDOWS_WIDTH,
                            0.05 * WINDOWS_HEIGHT,
                            RIGHT_CALLIBRATE_BUTTON,
                            "Callibrate player two",
                            normalize=1)
        menu = Button(0.025 * WINDOWS_WIDTH,
                      0.025 * WINDOWS_HEIGHT,
                      MENU_BUTTON,
                      "Menu",
                      normalize=1)
        screen.blit(im1, (0.05 * WINDOWS_WIDTH, 0.1 * WINDOWS_HEIGHT))
        screen.blit(im2, (0.75 * WINDOWS_WIDTH, 0.1 * WINDOWS_HEIGHT))
        play.draw(screen)
        r_call_btn.draw(screen)
        l_call_btn.draw(screen)
        menu.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                play.react_on_click(call_game, [screen, clock, template1, template2])
                l_call_btn.react_on_click(call_callibration, [screen, clock, template1 , 0])
                r_call_btn.react_on_click(call_callibration, [screen, clock, template2, 1])
                menu.react_on_click(return_to_menu)
        pygame.draw.rect(screen, COLOR, PLAYER_ONE_IMAGE, 2)
        pygame.draw.rect(screen, COLOR, PLAYER_TWO_IMAGE, 2)
        pygame.display.update()
