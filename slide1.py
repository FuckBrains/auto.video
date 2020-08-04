from config import *
from util import *

VIDEO_PATH = "video/"+VIDEO_SUB_PATH+"/slide1"+name_suffix+".mp4"
BG_PATH = "asset/"+ASSET_SUB_PATH+"slide1.jpg"
OBJ_PATH = "asset/"+TEMPLATE_PATH+"group3.png"

if AUTO_FIT_IMG:
	background_col = (ImageClip(BG_PATH).resize((w,h)).resize(1.5).resize(lambda t : 1-0.065*t).set_position(('center', 'center')).set_duration(DURATION))
else:
	background = ImageClip(BG_PATH)
	resize_factor = resize(background.size, VIDEO_SIZE)
	background = (ImageClip(BG_PATH).
		resize(resize_factor)
		.resize(1.5)
		.resize(lambda t : 1-0.065*t)
		.set_position('center', 'center')
		.set_duration(DURATION))
	background = background.fl_image( blur )
	avg_color = avg_color(BG_PATH)
	background_col = background.on_color(size=(VIDEO_SIZE),color=(avg_color[0],avg_color[1],avg_color[2]), pos=('center','center'), col_opacity=1)

logo = ImageClip(OBJ_PATH)
OBJ_RESIZE = 0.9/size_factor
obj_mar_w = int(logo.w *0.1)/2
obj_mar_h = int(logo.h *0.1)/2
logo = logo.set_position(('center', 'center')).resize(OBJ_RESIZE)

# A CLIP WITH A TEXT AND A BLACK SEMI-OPAQUE BACKGROUND

# txt = TextClip("AJNARA\nLe Garden", font=bold_font,color=font_color, fontsize=font_size, method='label', interline=5, kerning=9).margin(right=(obj_mar_w/size_factor)+10/size_factor, bottom=obj_mar_h/size_factor, opacity=0).set_pos(('center', 'center')).set_duration(DURATION - START_TIME).set_start(START_TIME).crossfadein(FADE_TIME + 0.25)
txt = TextClip("AJNARA\nLe Garden", font=bold_font,color=font_color, fontsize=font_size, method='label', interline=5, kerning=9).set_pos(('center', 'center')).set_duration(DURATION - START_TIME).set_start(START_TIME).crossfadein(FADE_TIME + 0.25)

# THE TEXT CLIP IS ANIMATED.

txt_mov = txt.set_pos( lambda t: ('center', max(w/4, min(w/2.5,int(w-0.5*w*t)))) ).set_duration(DURATION - START_TIME).set_start(START_TIME).crossfadein(FADE_TIME + 0.25)

# FINAL ASSEMBLY
final = CompositeVideoClip([background_col, logo, txt_mov], size=VIDEO_SIZE).set_duration(DURATION)
# effect = final.resize(1.25)
# final_clip = vfx.scroll(effect, w=w, x_speed=50, x_start=0)
final.write_videofile(VIDEO_PATH,fps=fps)