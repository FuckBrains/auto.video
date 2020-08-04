from config import *
from util import *

VIDEO_PATH = "video/"+VIDEO_SUB_PATH+"/slide2"+name_suffix+".mp4"
BG_PATH = "asset/"+ASSET_SUB_PATH+"slide2.jpg"
OBJ_PATH = "asset/"+TEMPLATE_PATH+"group.png"

if AUTO_FIT_IMG:
	background_col = (ImageClip(BG_PATH).resize((w,h)).resize(lambda t : 1+0.05*t).set_position(('center', 'center')).set_duration(DURATION))
else:
	background = ImageClip(BG_PATH)
	resize_factor = resize(background.size, VIDEO_SIZE)
	avg_color = avg_color(BG_PATH)
	background = (ImageClip(BG_PATH).
		resize(resize_factor).
		resize((w,h))
		.resize(lambda t : 1+0.05*t)
		.set_position('center', 'center')
		.set_duration(DURATION))
	background_col = background.on_color(size=(VIDEO_SIZE),color=(avg_color[0],avg_color[1],avg_color[2]), pos=('center','center'), col_opacity=1)

logo = ImageClip(OBJ_PATH)
OBJ_RESIZE = 0.9/size_factor
obj_mar_w = int(logo.w *0.1)/2
obj_mar_h = int(logo.h *0.1)/2
logo = logo.set_position(('center', 'center')).resize(OBJ_RESIZE)

# A CLIP WITH A TEXT AND A BLACK SEMI-OPAQUE BACKGROUND

# txt = TextClip("Sector 16", font=bold_font,color=font_color, fontsize=font_size, method='label', interline=interline, kerning=kerning).margin(right=obj_mar_w/size_factor, bottom=obj_mar_h/size_factor, opacity=0).set_pos(('center', 'center')).set_duration(DURATION - 0.7).set_start(TEXT_START_TIME).crossfadein(TEXT_START_TIME - 0.25)
# stxt = TextClip("Greater Noida", font=bold_font,color=font_color, fontsize=font_size_sub_txt, method='label', interline=interline, kerning=sub_kerning).margin(right=obj_mar_w/size_factor, bottom=obj_mar_h/size_factor, opacity=0).set_pos(('center', 400/size_factor)).set_duration(DURATION - TEXT_START_TIME).set_start(TEXT_START_TIME + 0.3).crossfadein(TEXT_START_TIME - 0.45)
stxt = TextClip("Sector 16, Greater Noida", font=bold_font,color=font_color, fontsize=font_size_sub_txt, method='label', interline=interline, kerning=sub_kerning).set_pos(('center', 400/size_factor)).set_duration(DURATION - TEXT_START_TIME).set_start(TEXT_START_TIME + 0.3).crossfadein(TEXT_START_TIME - 0.45)

# FINAL ASSEMBLY
final = CompositeVideoClip([background_col, logo, stxt], size=VIDEO_SIZE).set_duration(DURATION)
final.write_videofile(VIDEO_PATH,fps=fps)