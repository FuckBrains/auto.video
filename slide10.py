from config import *
from util import *

VIDEO_PATH = "video/"+VIDEO_SUB_PATH+"/slide10"+name_suffix+".mp4"
BG_PATH = "asset/"+ASSET_SUB_PATH+"slide3.png"
OBJ_PATH = "asset/"+TEMPLATE_PATH+"group-2.png"

font_size = 32
font_color = 'purple'


background = ImageClip(BG_PATH).set_position(('center', 'center'))

# A CLIP WITH A TEXT AND A BLACK SEMI-OPAQUE BACKGROUND

txt = TextClip("Property Amenities", font=bold_font,color='white', fontsize=font_size, method='label', interline=interline, kerning=kerning).set_position(('center',0.20), relative=True)
# stxt = TextClip("Housing.com", font=plain_font,color=font_color, fontsize=font_size, method='label', interline=35).set_pos(('center', 'center')).set_duration(DURATION - START_TIME).set_start(START_TIME).crossfadein(FADE_TIME)
stxt = TextClip("Pool", font=plain_font,color=font_color, fontsize=font_size, method='label', interline=35, size=(220,40), stroke_width=1, stroke_color="#4e20b1")
txt_col = stxt.on_color(size=(stxt.w+60,stxt.h+20),color=(255,255,255), col_opacity=0.99).set_position((0.1,0.30), relative=True)

stxt1 = TextClip("Pet Allowed", font=plain_font,color=font_color, fontsize=font_size, method='label', interline=35, size=(220,40), stroke_width=1, stroke_color="#4e20b1")
txt_col1 = stxt1.on_color(size=(stxt1.w+60,stxt1.h+20),color=(255,255,255), col_opacity=0.99).set_position((0.4,0.30), relative=True)

stxt2 = TextClip("Garden", font=plain_font,color=font_color, fontsize=font_size, method='label', interline=35, size=(220,40), stroke_width=1, stroke_color="#4e20b1")
txt_col2 = stxt2.on_color(size=(stxt2.w+60,stxt2.h+20),color=(255,255,255), col_opacity=0.99).set_position((0.7,0.30), relative=True)

stxt3 = TextClip("Gym", font=plain_font,color=font_color, fontsize=font_size, method='label', interline=35, size=(220,40), stroke_width=1, stroke_color="#4e20b1")
txt_col3 = stxt3.on_color(size=(stxt3.w+60,stxt3.h+20),color=(255,255,255), col_opacity=0.99).set_position((0.1,0.50), relative=True)

stxt4 = TextClip("Lift", font=plain_font,color=font_color, fontsize=font_size, method='label', interline=35, size=(220,40), stroke_width=1, stroke_color="#4e20b1")
txt_col4 = stxt4.on_color(size=(stxt4.w+60,stxt4.h+20),color=(255,255,255), col_opacity=0.99).set_position((0.4,0.50), relative=True)

stxt5 = TextClip("Intercom", font=plain_font,color=font_color, fontsize=font_size, method='label', interline=35, size=(220,40), stroke_width=1, stroke_color="#4e20b1")
txt_col5 = stxt5.on_color(size=(stxt5.w+60,stxt5.h+20),color=(255,255,255), col_opacity=0.99).set_position((0.7,0.50), relative=True)

stxt6 = TextClip("Sports Facility", font=plain_font,color=font_color, fontsize=font_size, method='label', interline=35, size=(220,40), stroke_width=1, stroke_color="#4e20b1")
txt_col6 = stxt6.on_color(size=(stxt6.w+60,stxt6.h+20),color=(255,255,255), col_opacity=0.99).set_position((0.1,0.70), relative=True)

stxt7 = TextClip("Kids Area", font=plain_font,color=font_color, fontsize=font_size, method='label', interline=35, size=(220,40), stroke_width=1, stroke_color="#4e20b1")
txt_col7 = stxt7.on_color(size=(stxt7.w+60,stxt7.h+20),color=(255,255,255), col_opacity=0.99).set_position((0.4,0.70), relative=True)

stxt8 = TextClip("Water Supply", font=plain_font,color=font_color, fontsize=font_size, method='label', interline=35, size=(220,40), stroke_width=1, stroke_color="#4e20b1")
txt_col8 = stxt8.on_color(size=(stxt8.w+60,stxt8.h+20),color=(255,255,255), col_opacity=0.99).set_position((0.7,0.70), relative=True)

# FINAL ASSEMBLY
final = CompositeVideoClip([background, txt, txt_col, txt_col1, txt_col2, txt_col3, txt_col4, txt_col5, txt_col6, txt_col7, txt_col8], size=VIDEO_SIZE).set_duration(DURATION)

final.write_videofile(VIDEO_PATH,fps=fps)