import math
import random
from settings import *
import pygame as pg
import time
import cv2
import statistics
import numpy as np
class Pad:
    def __init__(self,number,threshold=0.3,scale=500,delta=250):
        self.score=0
        self.image=pg.Surface((PAD_WIDTH*2,PAD_HEIGHT*2))
        self.image.fill((255,0,0))
        self.height=PAD_HEIGHT
        self.width=PAD_WIDTH
        self.threshold=threshold
        self.scale=scale
        self.delta=delta
        if number==1:
           self.pos=[PAD_WIDTH,WINDOWS_HEIGHT/2]
           
        elif number==2:
            self.pos=[WINDOWS_WIDTH-PAD_WIDTH,WINDOWS_HEIGHT/2]
        self.number=number
        
   
    def draw(self,screen):
        screen.blit(self.image,(self.pos[0]-self.width,self.pos[1]-self.height))
    def move(self,where,what,camera_res=480):    
        
        res = cv2.matchTemplate(where,what,cv2.TM_CCOEFF_NORMED)
        w, h = what.shape[::-1]
        loc = np.where( res >= self.threshold)
   
     
        Y=[]
        for pt in zip(*loc[::-1]):
       
            Y.append(pt[1])
        if Y==[]:
            return 
        mean_y=int(statistics.median(Y))
        self.pos[1]=((2*mean_y+h)/2/camera_res)*(WINDOWS_HEIGHT+self.scale)-self.delta
class Wall(Pad):
    def __init__(self,number):
        super().__init__(number)
        self.image=pg.Surface((PAD_WIDTH*2,WINDOWS_HEIGHT*10))
        self.image.fill((255,0,0))
        self.height=WINDOWS_HEIGHT*10
        self.width=PAD_WIDTH
        self.pos[1]=WINDOWS_WIDTH-self.width

class Ball:
    def __init__(self):
        
        self.pos=BALL_STARTPOS.copy()
        self.speed=BALL_SPEED
        self.generate_angle()
        self.acceleration=BALL_ACCELERATION
        self.image=pg.Surface((BALL_RADIUS*2,BALL_RADIUS*2))
        self.image.fill((0,255,0))
        self.last_hit=time.time()
        self.radius=BALL_RADIUS

    def move(self,dt,pad1,pad2):
        
        self.pos[0]+=dt*self.speed*self.vec_speed[0]
        self.pos[1]+=dt*self.speed*self.vec_speed[1]
        self.collide(pad1,pad2)
        
          
    def generate_angle(self):
        x=random.randint(30,90)/100*random.choice((-1,1))
        if x>0:
            y= 1-x
        else:
            y=1+x
        self.vec_speed=[x,y]
        print(self.vec_speed)

    def respawn(self,winner):
          self.generate_angle()
          self.speed=BALL_SPEED
          self.pos=BALL_STARTPOS.copy()
          winner.score+=1
    def update(self,screen):
       
         screen.blit(self.image,(self.pos[0]- self.radius,self.pos[1]- self.radius))
         
    
    def collide(self,pad1,pad2):
            
            if time.time()-self.last_hit>=1:
                if self.pos[0]+ self.radius>=pad2.pos[0]-pad1.width:  
                       if self.pos[1]+BALL_RADIUS>pad2.pos[1]-pad2.height and self.pos[1]- self.radius<pad2.pos[1]+pad2.height:
                         
                         self.vec_speed[0]=-self.vec_speed[0]
                         self.speed+=self.acceleration
                        
                if self.pos[0]- self.radius<=pad1.pos[0]+pad2.width:  
                  
                    if self.pos[1]+ self.radius>pad1.pos[1]-pad1.height and self.pos[1]- self.radius<pad1.pos[1]+pad1.height:
                         
                         self.vec_speed[0]=-self.vec_speed[0]
                         self.speed+=self.acceleration
           
                if self.pos[1]<WALLS[2]+ self.radius:   #top
                    self.vec_speed[1]=-self.vec_speed[1]
                    print(self.vec_speed)
                            
                if self.pos[1]>WALLS[3]- self.radius:  #bottom
                    self.vec_speed[1]=-self.vec_speed[1]
                    
                if self.pos[0]>WALLS[1]:
                    self.respawn(pad1)
                   
                if self.pos[0]<WALLS[0]:
                    self.respawn(pad2)
                  
             
