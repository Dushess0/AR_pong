import pygame
import image_choosing
from settings import *
import maingame_loop
from pygame.locals import *
import choose 
import cv2

MENU_PLAY = pygame.image.load('data/menu/PLAY.jpg')
MENU_OPTIONS = pygame.image.load('data/menu/OPTIONS.jpg')
MENU_EXIT = pygame.image.load('data/menu/EXIT.jpg')
WIN_WIDTH = 1920
WIN_HEIGHT = 1080
CLOCK = pygame.time.Clock()

pygame.init()
SWITCH_SOUND = pygame.mixer.Sound('data/sound_effects/DM-CGS-21.wav')

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("AR Pong")
pygame.mixer.music.load('data/Bluemillenium-Ivresse.mp3')
pygame.mixer.music.play(-1)
samples = {}
template1 = cv2.imread('green.jpg', 0)
template2 = cv2.imread('phone2.jpg', 0)

switch = 1
run = True
while run:

    if switch == 1:
        screen.blit(MENU_PLAY, (0, 0))
    elif switch == 2:
        screen.blit(MENU_OPTIONS, (0, 0))
    elif switch == 3:
        screen.blit(MENU_EXIT, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == K_w:
                switch += 1
                SWITCH_SOUND.play()

            elif event.key == K_DOWN or event.key == K_s:
                switch -= 1
                SWITCH_SOUND.play()

            elif event.key == K_RETURN:
                if switch == 1:
                    if 0 in samples.keys() and 1 in samples.keys():
                        if __name__ == '__main__':
                           
                            choose.main(screen,template1,template1,player1_im,player2_im)
                            maingame_loop.game_loop(screen,CLOCK,player1_im , player2_im)
                    else:
                        pass

                elif switch == 2:
                    
                    samples = image_choosing.main(screen, samples)
                    if 0 in samples.keys():
                        template1 = cv2.imread(samples[0], 0)

                        player1_im = pygame.image.load(samples[0])
                        player1_im =  pygame.transform.scale(player1_im, (int(0.2 * WINDOWS_WIDTH) , int(0.6 * WINDOWS_HEIGHT)) )

                    if 1 in samples.keys():
                        player2_im = pygame.image.load(samples[1])
                        player2_im = pygame.transform.scale(player2_im, (int(0.2 * WINDOWS_WIDTH),int(0.6 * WINDOWS_HEIGHT)))
                        template2 = cv2.imread(samples[1], 0)

                    print(samples)
                elif switch == 3:
                    run = False

    if switch == 4:
        switch = 1
    elif switch == 0:
        switch = 3

    pygame.display.update()
    CLOCK.tick(FPS)
