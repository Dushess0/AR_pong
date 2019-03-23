import pygame
from image_cropper import *
from settings import *
from os import path, walk
from pygame.locals import *

IMG_PLACE = (WINDOWS_WIDTH * 0.6, WINDOWS_HEIGHT * 0.4)


class Player_profile:
    def __init__(self, img_name, position, screen):
        self.position = position
        self.game_folder = path.join(path.dirname(__file__), "models")
        self.image_name = img_name
        self.image_path = path.join(self.game_folder, img_name)
        self.image = pygame.image.load(self.image_path)
        self.enlarged = pygame.transform.scale(self.image, (int(WINDOWS_WIDTH * 0.35), int(WINDOWS_HEIGHT * 0.5)))
        self.screen = screen
      
        self.exist = True

    def draw_image(self, profile):
        if self.image_path not in profile.values():
            self.screen.blit(self.enlarged, IMG_PLACE)
            pygame.display.update()
            return True
        else:
            return False


def read_directory(screen, filenames, models):

    for model in models:
        model.exist = False

    for root, dirs, files in walk("models"):
        for filename in files:
            find_model(filename, models)
            if filename not in filenames:
                filenames.append(filename)
                models.append(Player_profile(img_name=filename,
                                             position=[0, 0],
                                             screen=screen,
                                             ))
    clean_models(models)

def find_model(filename, models):
    for model in models:
        if filename == model.image_name:
            model.exist = True


def clean_models(models):
    for model in models:
        if not model.exist:
            models.remove(model)




def main(screen, samples):
  
    profile = samples

   
    FONT = pygame.font.Font(PLAYER_NUMBER_FONT, 85)
    FONT_SHADOW = pygame.font.Font(PLAYER_NUMBER_FONT, 85)
    MENU_OPTIONS = pygame.image.load(OPTIONS_BACKGROUND)
    MENU_OPTIONS=pygame.transform.scale(MENU_OPTIONS,(WINDOWS_WIDTH,WINDOWS_HEIGHT))
    SWITCH_SOUND = pygame.mixer.Sound(MENU_BUTTON_SOUND)
    switch = 1
    run_options = True

    player_names = {0: "PLAYER ONE", 1: "PLAYER TWO"}

    player_one_id = 0
    player_two_id = 1
    # current player
    current_player = player_one_id

    filenames = []
    models = []
    read_directory(screen, filenames, models)
  
    index_of_current_image_profile = 0
 
    while run_options:
        screen.blit(MENU_OPTIONS, (0, 0))
     
        if switch == 1:
            player_text_shadow = FONT_SHADOW.render(player_names[current_player], False, Color(PLAYER_NUMBER_COLOR))
            screen.blit(player_text_shadow, (277, 118))

        player_text = FONT.render(player_names[current_player], False, Color(PLAYER_NUMBER_SHADOW_COLOR))
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
                    read_directory(screen, filenames, models)
                    while not models[index_of_current_image_profile % len(models)].draw_image(profile):
                        index_of_current_image_profile = (index_of_current_image_profile + 1) % len(models)
                    index_of_current_image_profile = (index_of_current_image_profile + 1) % len(models)

                elif event.key == K_LEFT or event.key == K_d:
                    read_directory(screen,filenames,models)
                    if index_of_current_image_profile > 0:
                        index_of_current_image_profile -= 1
                    elif index_of_current_image_profile == 0:
                        index_of_current_image_profile = len(models) - 1
                    while not models[index_of_current_image_profile % len(models)].draw_image(profile):
                        index_of_current_image_profile = (index_of_current_image_profile - 1)
                    models[index_of_current_image_profile].draw_image(profile)
                    screen.blit(player_text, (275, 120))

                elif event.key == K_c:
                    make_a_sample(screen)
                    read_directory(screen, filenames, models)
               
                elif event.key == K_RETURN:
                  
                    screen.blit(MENU_OPTIONS, (0, 0))
                    profile[current_player] = models[index_of_current_image_profile].image_path          
                    current_player = not current_player
                elif event.key == K_ESCAPE:
                    run_options = False
                    return profile

        models[index_of_current_image_profile].draw_image(profile)
        pygame.display.update()
