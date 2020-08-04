from config import *

VIDEO_PATH = "video/"+VIDEO_SUB_PATH+"/slide3.mp4"
BG_PATH = "asset/"+ASSET_SUB_PATH+"slide3.jpg"
OBJ_PATH = "asset/"+TEMPLATE_PATH+"group.png"
font_size = 32
font_size_sub_txt = 26

background = (ImageClip(BG_PATH). \
        resize((w,h)).
        resize(lambda t : 1+0.05*t)
        .set_position('center', 'center')
        .set_duration(DURATION))

logo = ImageClip(OBJ_PATH). \
        set_position(('center', 'center')).resize(0.9)

logo_mov = logo.set_position( lambda t: (490, 'center')).set_duration(DURATION - START_TIME).set_start(START_TIME).crossfadein(FADE_TIME)

# A CLIP WITH A TEXT AND A BLACK SEMI-OPAQUE BACKGROUND

txt = TextClip("Sector 32", font=bold_font,color=font_color, fontsize=font_size, method='label', interline=15, kerning=4).set_pos(('center', 'center')).set_duration(DURATION - 0.7).set_start(TEXT_START_TIME).crossfadein(TEXT_START_TIME - 0.25)
stxt = TextClip("Gurgaon", font=bold_font,color=font_color, fontsize=font_size_sub_txt, method='label', interline=15, kerning=4).set_pos(('center', 400)).set_duration(DURATION - TEXT_START_TIME).set_start(TEXT_START_TIME + 0.3).crossfadein(TEXT_START_TIME - 0.45)


# FINAL ASSEMBLY
final = CompositeVideoClip([background, logo_mov, txt, stxt], size=VIDEO_SIZE).set_duration(DURATION)
final.write_videofile(VIDEO_PATH,fps=fps)