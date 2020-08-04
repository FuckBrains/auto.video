from moviepy.editor import *

size_factor = 1
if size_factor == 1:
	name_suffix = ""
else:
	name_suffix = "_"+str(size_factor)
VIDEO_SIZE = (1280/size_factor, 720/size_factor)
DURATION = 4
START_TIME = 0.5
FADE_TIME = 0.75
TEXT_START_TIME = 1
VIDEO_SUB_PATH = "rental/prop4/"
ASSET_SUB_PATH = "rental/prop4/"
TEMPLATE_PATH = "template2/"
VIDEO_PATH = "video/"+VIDEO_SUB_PATH+"slide99.mp4"
w,h=(1280/size_factor, 720/size_factor)
fps = 20
BG_PATH = 'asset/bgrect1.png'
OBJ_PATH = 'asset/housing.png'
plain_font = 'Helvetica'
bold_font = 'Helvetica-Bold'
font_size = 32/size_factor
font_size_medium = 40/size_factor
font_size_large = 75/size_factor
font_size_sub_txt = 22/size_factor
kerning = 4/size_factor
sub_kerning = 2/size_factor
interline = 15/size_factor
font_color = 'white'
delay = 1
#BG_AUDIO = "asset/demo_music.mp3"
BG_AUDIO = "asset/music_clip_2.mp3"
AUTO_FIT_IMG = True
DESCRIPTION_TEXT_COUNT = 525