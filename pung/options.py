import pygame
from pygame.locals import *


def main(screen):
    pygame.font.init()
    FONT = pygame.font.Font("data/font/Anurati-Regular.otf", 90)
    FONT_SHADOW = pygame.font.Font("data/font/Anurati-Regular.otf", 90)
    MENU_OPTIONS = pygame.image.load('data/options/tmp.jpg')
    SWITCH_SOUND = pygame.mixer.Sound('data/sound_effects/DM-CGS-21.wav')
    switch = 1
    run_options = True

    player_one_name = "PLAYER ONE"
    player_two_name = "PLAYER TWO"

    while run_options:

        screen.blit(MENU_OPTIONS, (0, 0))

        if switch == 1:
            player_text_shadow = FONT_SHADOW.render(player_one_name, False, Color("#9400D3"))
            screen.blit(player_text_shadow, (205, 95))

        player_text = FONT.render(player_one_name, False, Color("#FF4500"))
        screen.blit(player_text, (200, 100))

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
