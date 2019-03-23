
#game options
PAD_WIDTH=15
PAD_HEIGHT=70
BALL_RADIUS=15
WINDOWS_HEIGHT=900
WINDOWS_WIDTH=1200
BALL_SPEED=200
BALL_ACCELERATION=50
BALL_STARTPOS=[WINDOWS_WIDTH/2,WINDOWS_HEIGHT/2]
WALLS=[0,WINDOWS_WIDTH,0,WINDOWS_HEIGHT]
FPS=60


DEFAULT_HEIGHT=1080  # dont change
DEFAULT_WIDTH=1980   # dont change
#image recognition

CALLIBRATION_FILE="callibration_values.json"
calib_data = [{'scale': 500, 'delta': 250, 'threshold': 0.3},{'scale': 500, 'delta': 250, 'threshold': 0.3}]

#images, fonts and audio
MENU_BUTTON_SOUND='data/sound_effects/DM-CGS-21.wav'
USUAL_FONT="data/calibri.ttf"
SOUNDTRACK='data/Bluemillenium-Ivresse.mp3'
MENU_EXIT_IMAGE='data/menu/EXIT.jpg'
MENU_OPTIONS_IMAGE='data/menu/OPTIONS.jpg'
MENU_PLAY_IMAGE='data/menu/PLAY.jpg'
OPTIONS_BACKGROUND='data/menu/OPTIONS_MAIN.jpg'
FONT_SCALE=(WINDOWS_HEIGHT*WINDOWS_WIDTH)/(DEFAULT_HEIGHT*DEFAULT_WIDTH)
SAMPLES_FOLDER="models/"
PLAYER_NUMBER_FONT="data/Anurati-Regular.otf"
PLAYER_NUMBER_COLOR="#ba157e"
PLAYER_NUMBER_SHADOW_COLOR="#df8f2f"

