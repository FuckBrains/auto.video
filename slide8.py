from __future__ import division
from config import *
from util import *

def object_position(template):
	print(template)
	if template == 'template2/':
		return ('center', 0.8)
	else:
		return ('left', 0.8)

def object_txt_position(template):
	print(template)
	if template == 'template2/':
		return ('center', 0.84)
	else:
		return (0.04, 0.84)

VIDEO_PATH = "video/"+VIDEO_SUB_PATH+"/slide8"+name_suffix+".mp4"
BG_PATH = "asset/"+ASSET_SUB_PATH+"slide8.jpg"
OBJ_PATH = "asset/"+TEMPLATE_PATH+"group2.png"

if AUTO_FIT_IMG:
	background_col = (ImageClip(BG_PATH).resize((w,h)).resize(1.5).resize(lambda t : 1-0.065*t).set_position(('center', 'center')).set_duration(DURATION))
else:
	background = ImageClip(BG_PATH)
	resize_factor = resize(background.size, VIDEO_SIZE)
	background = (ImageClip(BG_PATH).resize(resize_factor * (1.5))
			.resize(lambda t : 1-0.065*t)
			.set_position('center', 'center')
			.set_duration(DURATION))
	avg_color = avg_color(BG_PATH)
	invert_color = invert_color(avg_color)
	background_col = background.on_color(size=(VIDEO_SIZE),color=(avg_color[0],avg_color[1],avg_color[2]), pos=('center','center'), col_opacity=1)

logo = ImageClip(OBJ_PATH).resize((630/size_factor, 90/size_factor))

logo_mov = logo.set_position( object_position(TEMPLATE_PATH), relative=True).set_duration(DURATION - START_TIME).set_start(START_TIME).crossfadein(FADE_TIME)
# logo_mov = logo.set_position( lambda t: ('left', 0.8), relative=True).set_duration(DURATION - START_TIME).set_start(START_TIME).crossfadein(FADE_TIME)

# A CLIP WITH A TEXT AND A BLACK SEMI-OPAQUE BACKGROUND

txt = TextClip("Nearby Schools/Universities - 2", font=bold_font,color=font_color, fontsize=font_size, method='label', interline=interline, kerning=kerning).set_pos(object_txt_position(TEMPLATE_PATH), relative=True).set_duration(DURATION  - 0.7).set_start(START_TIME + START_TIME).crossfadein(FADE_TIME + 0.25)


# FINAL ASSEMBLY
final = CompositeVideoClip([background_col, logo_mov, txt], size=VIDEO_SIZE).set_duration(DURATION)
final.write_videofile(VIDEO_PATH,fps=fps)