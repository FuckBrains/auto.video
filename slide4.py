# -*- coding: utf-8 -*-
from __future__ import division
from config import *
from util import *

VIDEO_PATH = "video/"+VIDEO_SUB_PATH+"/slide4"+name_suffix+".mp4"
BG_PATH = "asset/"+ASSET_SUB_PATH+"slide4.jpg"
OBJ_PATH = "asset/"+TEMPLATE_PATH+"group1.png"
t = u'\u20B9 ₹ Rs 71.8 L'.encode('utf-8')
raw_text = u"\u20B9"

if AUTO_FIT_IMG:
	background_col = ImageClip(BG_PATH).resize((w,h)).set_position(('center', 'center'))
else:
	background = ImageClip(BG_PATH)
	resize_factor = resize(background.size, VIDEO_SIZE)
	background = ImageClip(BG_PATH). \
		set_position(('center', 'center')).resize(resize_factor)
	avg_color = avg_color(BG_PATH)
	invert_color = invert_color(avg_color)
	background_col = background.on_color(size=(VIDEO_SIZE),color=(avg_color[0],avg_color[1],avg_color[2]), pos=('center','center'), col_opacity=0.75)

logo = ImageClip(OBJ_PATH).set_position((0.4,0.7), relative=True).resize(1/size_factor)
# logo = ImageClip(OBJ_PATH).resize((461, 335)).resize(1/size_factor)
# logo_mov = logo.set_position( lambda t: ('right', 0.57), relative=True).set_duration(DURATION - START_TIME).set_start(START_TIME).crossfadein(FADE_TIME)
logo_mov = logo.set_position( lambda t: ('right', 'bottom'), relative=True).set_duration(DURATION - START_TIME).set_start(START_TIME).crossfadein(FADE_TIME)

# A CLIP WITH A TEXT AND A BLACK SEMI-OPAQUE BACKGROUND

# txt = TextClip("3 BHK", font=bold_font,color=font_color, fontsize=font_size, method='label', interline=interline, kerning=kerning).set_pos((0.674, 0.727), relative=True).set_duration(DURATION - 0.7).set_start(1).crossfadein(FADE_TIME + 0.25)
# stxt = TextClip("Rs 12000", font=bold_font,color=font_color, fontsize=font_size, method='label', interline=15, kerning=sub_kerning).set_pos((0.833, 0.727), relative=True).set_duration(DURATION - 0.8).set_start(1.1).crossfadein(FADE_TIME + 0.05)

txt = TextClip("2 BHK\nApartments", font=bold_font,color=font_color, fontsize=font_size, method='label', interline=interline, kerning=kerning).set_pos((0.65, 0.80), relative=True).set_duration(DURATION - 0.7).set_start(1).crossfadein(FADE_TIME + 0.25)
stxt = TextClip("Rent\nRs 27000", font=bold_font,color=font_color, fontsize=font_size_sub_txt, method='label', interline=15, kerning=sub_kerning).set_pos((0.91, 0.825), relative=True).set_duration(DURATION - 0.8).set_start(1.1).crossfadein(FADE_TIME + 0.05)

# FINAL ASSEMBLY
final = CompositeVideoClip([background_col, logo_mov, txt, stxt], size=VIDEO_SIZE).set_duration(DURATION)
# scrollLeft = final.resize((w+(300/size_factor),h))
# flinal_clip = vfx.scroll(scrollLeft, w=w, h=h, x_speed=100/size_factor, x_start=50/size_factor)
# flinal_clip.write_videofile(VIDEO_PATH,fps=fps)
final.write_videofile(VIDEO_PATH,fps=fps)