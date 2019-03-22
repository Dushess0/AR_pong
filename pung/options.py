import pygame
from crop import  *
from settings import *
from os import path , walk
from pygame.locals import *

class Player_profile:
    def __init__(self, img_name , position , screen ):
        self.position = position
        self.game_folder = path.join(path.dirname(__file__), "models")
        self.image_name = img_name
        self.image_path = path.join(self.game_folder, img_name)
        self.image = pygame.image.load(self.image_path)
        self.enlarged = pygame.transform.scale(self.image, (int(WINDOWS_WIDTH * 0.25) ,int(WINDOWS_HEIGHT * 0.25)))
        self.screen = screen
        self.start_position =  WINDOWS_HEIGHT * 0.3
        # self.color = (255 , 255 , 255 )
        self.item_height = WINDOWS_HEIGHT * 0.5 / 5
        self.item_width = WINDOWS_WIDTH * 0.3
        self.rect = ( position[0] ,position[1]  + self.start_position ,  self.item_width , self.item_height )
        #is object selected now
        self.active = False
    #
    # def change_color(self):
    #     if self.active:
    #         self.color = (102, 255, 204, 0.5)
    #     else:
    #         self.color = (255 , 255 , 255 , 0)



    def draw_image(self):
        pygame.draw.rect(self.screen, ACTIVE, IMAGE_PLACE, 2)
        self.screen.blit(self.enlarged, IMG_PLACE)
        print(self.image_path)
        pygame.display.update()



def read_directory(screen , filenames , models):

    for root, dirs, files in walk("models"):
        for filename in files:
            if filename not in filenames:

                filenames.append(filename)
                models.append(Player_profile(img_name=filename,
                               position=[0 , 0 ],
                               screen=screen,
                               ))

def print_object (models , screen , font):
    for model in models:
        text = font.render(model.id, True, (0, 128, 0))
        screen.blit(text,
                    (  (model.position[0]  + model.item_width) / 2, model.position[1] ))
    pygame.display.update()

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

    filenames = []
    models = []
    models[0].draw_image()
    i = 1

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
                elif event.key == K_RIGHT or event.key == K_a:
                    models[i].draw_image()
                    if i < len(models) - 1 :
                        i += 1
                elif event.key == K_LEFT or event.key == K_d:
                    if i > 0:
                        i -= 1
                    models[i].draw_image()
                elif event.key == K_c:
                    make_a_sample()
                    read_directory(screen , filenames , models)


                elif event.key == K_RETURN:
                    if switch == 1:
                        print("enter")

                elif event.key == K_ESCAPE:
                    run_options = False

        pygame.display.update()
