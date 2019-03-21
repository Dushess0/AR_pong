import pygame
from pygame.locals import *


def main(screen):
    pygame.font.init()
    FONT = pygame.font.Font("data/Anurati-Regular.otf", 85)
    FONT_SHADOW = pygame.font.Font("data/Anurati-Regular.otf", 85)
    MENU_OPTIONS = pygame.image.load('data/menu/OPTIONS_MAIN.jpg')
    SWITCH_SOUND = pygame.mixer.Sound('data/sound_effects/DM-CGS-21.wav')
    switch = 1
    run_options = True

    player_one_name = "PLAYER ONE"
    player_two_name = "PLAYER TWO"

    while run_options:

        screen.blit(MENU_OPTIONS, (0, 0))

        if switch == 1:
            player_text_shadow = FONT_SHADOW.render(player_one_name, False, Color("#ba157e"))
            screen.blit(player_text_shadow, (277, 118))

        player_text = FONT.render(player_one_name, False, Color("#df8f2f"))
        screen.blit(player_text, (275, 120))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_UP or event.key == K_w:
                    switch += 1
                    SWITCH_SOUND.play()
                elif event.key == K_DOWN or event.key == K_s:
                    switch -= 1
                    SWITCH_SOUND.play()

                elif event.key == K_RETURN:
                    if switch == 1:
                        print("enter")

                elif event.key == K_ESCAPE:
                    run_options = False

        pygame.display.update()
