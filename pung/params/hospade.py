import pygame
from settings import *
from pygame.locals import *
from objects import*
import cv2

CLOCK = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))
pygame.display.set_caption("AR Pong")
pygame.font.init()

    

def player_test(template1):
    player_1=Pad(1)
    player_2=Wall(2)
    ball=Ball()
    exit=Exit(150,25,(WINDOWS_WIDTH-190,WINDOWS_HEIGHT-25),"Exit")
    buttons=[
        Button(150,25,(WINDOWS_WIDTH/2,25),"DELTA",start_value=250),
         Button(150,25,(WINDOWS_WIDTH/2,80),"SCALE",start_value=500),
         Button(150,25,(WINDOWS_WIDTH/2,WINDOWS_HEIGHT-25),"THRESHOLD",start_value=0.3),
                ]

    buttons.append(ArrowButton(buttons[0],5,"left",width=25,height=25,pos=(WINDOWS_WIDTH/2-190,25),font_size=15))
    buttons.append(ArrowButton(buttons[0],5,"right",width=25,height=25,pos=(WINDOWS_WIDTH/2+190,25),font_size=15))

    buttons.append(ArrowButton(buttons[1],10,"left",width=25,height=25,pos=(WINDOWS_WIDTH/2-190,80),font_size=15))
    buttons.append(ArrowButton(buttons[1],10,"right",width=25,height=25,pos=(WINDOWS_WIDTH/2+190,80),font_size=15))

    buttons.append(ArrowButton(buttons[2],0.025,"left",width=25,height=25,pos=(WINDOWS_WIDTH/2-190,WINDOWS_HEIGHT-25),font_size=15))
    buttons.append(ArrowButton(buttons[2],0.025,"right",width=25,height=25,pos=(WINDOWS_WIDTH/2+190,WINDOWS_HEIGHT-25),font_size=15))

    capture=cv2.VideoCapture(0)  
    ret,frame=capture.read()
    image=cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    
    x,camera_res=img_gray.shape[::-1]
    del x,img_gray,image
    data=None
    running=True
    while running:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
            

                if event.key == K_RETURN:
                      player_1.pos[1]+=10
                if event.key==K_i:
                      player_1.pos[1]-=10
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    button.react_on_click()
                exit.react_on_click(buttons)
                if exit.data!={}:
                    running=False
        ret,frame=capture.read()
        
        image=cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        player_1.move(img_gray,template1,camera_res)
        for button in buttons:
            button.draw(screen)
        exit.draw(screen)
        player_1.draw(screen)
        player_1.delta=buttons[0].value
        player_1.scale=buttons[1].value
        player_1.threshold=buttons[2].value
        player_2.draw(screen)
        ball.move(1/FPS,player_1,player_2)
        ball.update(screen)
        
        pygame.display.update()
        
        CLOCK.tick(FPS)
    return exit.data

template1=cv2.imread("green.jpg",0)
print(player_test(template1))





