
import pygame as pg


class Button:
    def __init__(self, width, height, pos, text="", font="calibri.ttf", button_color=(128, 128, 128), font_size=32,
                 font_pos=(10, 10), font_color=(255, 0, 0), start_value=50,isCentered=True):
        self.width = width
        self.height = height
        self.pos = pos
        self.text = text
        self.font = font
        self.font_size = font_size
        self.font_pos = font_pos
        self.font_color = font_color
        self.button_color = button_color
        self.value = start_value
        self.update_text(self.text)
        if  not isCentered:
            self.pos=[self.pos[0]+self.width,self.pos[1]+self.height]

    def react_on_click(self, function, arg=None):

        x, y = pg.mouse.get_pos()
        if x > self.pos[0] - self.width and x < self.pos[0] + self.width:
            if y > self.pos[1] - self.height and y < self.pos[1] + self.height:
                if arg.any():
                    self.action(function, arg)
                else:
                    self.action()

    def action(self, function, arg=None):
        if arg.any():
            function(arg)


    def draw(self, screen):
        screen.blit(self.image, (self.pos[0] - self.width, self.pos[1] - self.height))




    def update_text(self, text):
        self.text = text
        FONT = pg.font.Font(self.font, self.font_size)
        self.image = pg.Surface((self.width * 2, self.height * 2))
        self.image.fill(self.button_color)
        FONT = FONT.render(text, False, self.font_color)
        self.image.blit(FONT, self.font_pos)



        
class Button:
    def __init__(self,width,height,pos,text="",font="calibri.ttf",button_color=(128,128,128),font_size=32,font_pos=(10,10),font_color=(255,0,0),start_value=50):
        self.width=width
        self.height=height
       
        self.pos=pos
        self.text=text
        self.font=font
        self.font_size=font_size
        self.font_pos=font_pos
        self.font_color=font_color
        self.button_color=button_color
        self.value=start_value
        self.update_text(self.text)
        self.pos=[self.pos[0]+self.width,self.pos[1]+self.height]
        
    def react_on_click(self,arg=None):

            x,y=pg.mouse.get_pos()
            if x>self.pos[0]-self.width and x<self.pos[0]+self.width:
                if y>self.pos[1]-self.height and y<self.pos[1]+self.height:
                    if arg!=None:
                       self.action(arg)
                    else:
                        self.action()
    def action(self,arg=None):
         pass
    def draw(self,screen):
         screen.blit(self.image,(self.pos[0]-self.width,self.pos[1]-self.height))
    def update_text(self,text):
        self.text=text
        FONT = pg.font.Font(self.font,self.font_size)
        self.image=pg.Surface(( self.width*2,self.height*2))
        self.image.fill(self.button_color)
        FONT=FONT.render(text, False,self.font_color)
        self.image.blit(FONT,self.font_pos)
class ArrowButton(Button):
    def __init__(self,container,delta,side,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.container=container
        self.side=side
        self.delta=delta
    def action(self):
        if self.side=="right":
           self.container.value+=self.delta
        else:
            self.container.value-=self.delta
        self.container.update_text(str(round(self.container.value,5)))

class Exit(Button):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.data={}
   
    def action(self,buttons):
        self.data={"scale":buttons[1].value,"delta":buttons[0].value,"threshold":buttons[2].value}
       
