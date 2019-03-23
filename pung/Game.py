import pygame
import image_choosing
from settings import *
import maingame_loop
from pygame.locals import *
import choose 
import cv2

MENU_PLAY = pygame.image.load(MENU_PLAY_IMAGE)
MENU_OPTIONS = pygame.image.load(MENU_OPTIONS_IMAGE)
MENU_EXIT = pygame.image.load(MENU_EXIT_IMAGE)

MENU_PLAY=pygame.transform.scale(MENU_PLAY,(WINDOWS_WIDTH,WINDOWS_HEIGHT))
MENU_OPTIONS=pygame.transform.scale(MENU_OPTIONS,(WINDOWS_WIDTH,WINDOWS_HEIGHT))
MENU_EXIT=pygame.transform.scale(MENU_EXIT,(WINDOWS_WIDTH,WINDOWS_HEIGHT))


CLOCK = pygame.time.Clock()

pygame.init()
pygame.font.init()
SWITCH_SOUND = pygame.mixer.Sound(MENU_BUTTON_SOUND)

screen = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))
pygame.display.set_caption("AR Pong")
pygame.mixer.music.load(SOUNDTRACK)
pygame.mixer.music.play(-1)
samples = {}
template1 = None
template2 = None

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
                            screen.fill((0,0,0))
                            choose.main(screen , CLOCK, samples[0] , samples[1] , player1_im , player2_im)
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

                  
                elif switch == 3:
                    run = False

    if switch == 4:
        switch = 1
    elif switch == 0:
        switch = 3

    pygame.display.update()
    CLOCK.tick(FPS)
