from config import *
from util import *

VIDEO_PATH = "video/"+VIDEO_SUB_PATH+"slide0"+name_suffix+".mp4"
BG_PATH = "asset/"+ASSET_SUB_PATH+"slide0.jpg"

if AUTO_FIT_IMG:
	background_col = ImageClip(BG_PATH).resize((w,h)).set_position(('center', 'center'))
else:
	background = ImageClip(BG_PATH)
	resize_factor = resize(background.size, VIDEO_SIZE)
	background = ImageClip(BG_PATH).set_position(('center', 'center')).resize(resize_factor)
	avg_color = avg_color(BG_PATH)
	invert_color = invert_color(avg_color)
	background_col = background.on_color(size=(VIDEO_SIZE),color=(avg_color[0],avg_color[1],avg_color[2]), pos=('center','center'), col_opacity=0.75)
# A CLIP WITH A TEXT AND A BLACK SEMI-OPAQUE BACKGROUND


txt = TextClip("Welcome to", font=plain_font,color=font_color, fontsize=font_size)
# .margin(bottom=130/size_factor, opacity=0)
# stxt = TextClip("The House of Your Dreams", font='Helvetica',color='white', fontsize=40, size=(480,40)).set_pos((80, 600)).set_duration(DURATION - (START_TIME + 1)).set_start(START_TIME + 1).crossfadein(FADE_TIME)
stxt = TextClip("2 BHK Semi Furnished Apartment", font=plain_font,color=font_color, fontsize=font_size_medium)

txt_col = txt.on_color(size=(txt.w+(50/size_factor),txt.h+(30/size_factor)),color=(105,14,200), pos=('center','center'), col_opacity=0.87)
stxt_col = stxt.on_color(size=(stxt.w+(50/size_factor),stxt.h+(30/size_factor)),color=(0,0,0), pos=('center','center'), col_opacity=0.85).margin(left=80/size_factor, bottom=60/size_factor, opacity=0).set_pos(('left', 'bottom')).set_duration(DURATION - (START_TIME + 1)).set_start(START_TIME + 1).crossfadein(FADE_TIME)

# THE TEXT CLIP IS ANIMATED.

txt_mov = txt_col.set_pos( lambda t: (max(w/16,int(w-0.5*w*t*t*t)), 520/size_factor) ).set_duration(DURATION - START_TIME).set_start(START_TIME).crossfadein(FADE_TIME)



# FINAL ASSEMBLY
final = CompositeVideoClip([background_col, txt_mov, stxt_col], size=VIDEO_SIZE).set_duration(DURATION)
final.write_videofile(VIDEO_PATH,fps=fps)