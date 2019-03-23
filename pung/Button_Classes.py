import pygame as pg
from settings import USUAL_FONT,FONT_SCALE



class Button:
    def __init__(self, width, height, pos, text="", font=USUAL_FONT, button_color=(128, 128, 128), font_size=64,
                  font_color=(255, 0, 0), start_value=50 , normalize = 0):
        self.width = width
        self.height = height

        self.pos = pos
        self.text = text
        self.font = font
        self.font_size = font_size
        
        self.font_size= int(font_size*FONT_SCALE)
        lenght=len(text)
        print(self.text)
        print(self.pos)
        print(self.width)
        print(self.height)
        
       
    
        self.font_color = font_color
        self.button_color = button_color
        self.value = start_value
        self.update_text(self.text)
        if normalize:
            self.pos = [self.pos[0] + self.width, self.pos[1] + self.height]

    def react_on_click(self, function=None, arg=None):

        x, y = pg.mouse.get_pos()
        if x > self.pos[0] - self.width and x < self.pos[0] + self.width:
            if y > self.pos[1] - self.height and y < self.pos[1] + self.height:
                
                self.action(function, arg)

    def action(self, function=None, arg=None):
        if arg != None:
            function(arg)
        elif function!=None:
            function()

    def draw(self, screen):
        screen.blit(self.image, (self.pos[0] - self.width, self.pos[1] - self.height))

    def update_text(self, text):
        self.text = text
        FONT = pg.font.Font(self.font, self.font_size)
        self.image = pg.Surface((self.width * 2, self.height * 2))
        self.image.fill(self.button_color)
        FONT = FONT.render(text, False, self.font_color)
        lenght=len(text)
        self.font_pos = [(self.width-lenght*self.font_size/4),(self.height-self.font_size/2)]
        self.image.blit(FONT, self.font_pos)


class ArrowButton(Button):
    def __init__(self, container, delta, side, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.container = container
        self.side = side
        self.delta = delta

    def action(self,function=None,arg=None):
        if self.side == "right":
            self.container.value += self.delta
        else:
            self.container.value -= self.delta
        self.container.update_text(str(round(self.container.value, 5)))


class Exit(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = {}

    def action(self, buttons, function=None,arg=None):
        self.data = {"scale": buttons[1].value, "delta": buttons[0].value, "threshold": buttons[2].value}
