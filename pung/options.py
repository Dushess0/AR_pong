import pygame
from crop import  *
from settings import *
from os import path , walk
from pygame.locals import *

IMG_PLACE = ( WIN_WIDTH * 0.6 ,WIN_HEIGHT * 0.4)

class Player_profile:
    def __init__(self, img_name , position , screen ):
        self.position = position
        self.game_folder = path.join(path.dirname(__file__), "models")
        self.image_name = img_name
        self.image_path = path.join(self.game_folder, img_name)
        self.image = pygame.image.load(self.image_path)
        self.enlarged = pygame.transform.scale(self.image, (int(WIN_WIDTH * 0.35) ,int(WIN_HEIGHT * 0.5)))
        self.screen = screen
        # self.color = (255 , 255 , 255 )
        # self.item_height = WIN_HEIGHT * 0.5 / 5
        # self.item_width = WIN_WIDTH * 0.3
        #is object selected now
        self.active = False


    def draw_image(self , profile):
        if self.image_path not in profile.values():
            self.screen.blit(self.enlarged, IMG_PLACE)
            pygame.display.update()
            return True
        else:
            return False



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

def main(screen , samples):

    #dictionary of profile images pathes
    profile = samples


    pygame.font.init()
    FONT = pygame.font.Font("data/Anurati-Regular.otf", 85)
    FONT_SHADOW = pygame.font.Font("data/Anurati-Regular.otf", 85)
    MENU_OPTIONS = pygame.image.load('data/menu/OPTIONS_MAIN.jpg')
    SWITCH_SOUND = pygame.mixer.Sound('data/sound_effects/DM-CGS-21.wav')
    switch = 1
    run_options = True

    player_names = {0:"PLAYER ONE" , 1:"PLAYER TWO"}


    player_one_id = 0
    player_two_id = 1
    #current player
    current_player = player_one_id

    filenames = []
    models = []
    read_directory(screen , filenames , models)
    models[0].draw_image(profile)
    i = 1
    #here
    screen.blit(MENU_OPTIONS, (0, 0))
    #
    while run_options:
        # moved upper to prevent unstoppable updating of background
        # screen.blit(MENU_OPTIONS, (0, 0))
        #

        if switch == 1:
            player_text_shadow = FONT_SHADOW.render(player_names[current_player], False, Color("#ba157e"))
            screen.blit(player_text_shadow, (277, 118))

        player_text = FONT.render(player_names[current_player], False, Color("#df8f2f"))
        screen.blit(player_text, (275, 120))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_UP or event.key == K_w:
                    switch += 1
                    SWITCH_SOUND.play()
                    screen.blit(player_text, (275, 120))

                elif event.key == K_DOWN or event.key == K_s:
                    switch -= 1
                    SWITCH_SOUND.play()
                    screen.blit(player_text, (275, 120))

                elif event.key == K_RIGHT or event.key == K_a:
                    while not models[i].draw_image(profile) :
                        i =  (i + 1 ) % len(models)
                    i = (i + 1) % len(models)

                elif event.key == K_LEFT or event.key == K_d:
                    if i > 0:
                        i -= 1
                    elif i == 0:
                        i = len(models) - 1
                    while not models[i].draw_image(profile):
                        i =  (i - 1 )
                    models[i].draw_image(profile)
                    screen.blit(player_text, (275, 120))

                elif event.key == K_c:
                    make_a_sample()
                    read_directory(screen , filenames , models)
                #accept picture and change the player
                elif event.key == K_o:
                    #accept
                    screen.blit(MENU_OPTIONS, (0, 0))
                    profile[current_player] = models[i].image_path
                    #to write in more grammarly correct form
                    current_player = not current_player




                elif event.key == K_RETURN:
                    if switch == 1:
                        print("enter")

                elif event.key == K_ESCAPE:
                    run_options = False
                    return profile

        pygame.display.update()
