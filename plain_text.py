from moviepy.editor import *

VIDEO_SIZE = (1280, 720)
DURATION = 2.5
w,h=(1280, 720)
BG_PATH = 'BG image.jpg'
LOGO_PATH = 'housing.png'
bold_font = 'Liberation-Sans-Bold'
plain_font = 'Liberation-Sans'

background = ImageClip(BG_PATH). \
        set_position(('center', 'center')).set_fps(120)

logo = ImageClip(LOGO_PATH). \
        set_position(('center', 'center')).resize(width=70)

# logo_mov = logo.set_position( lambda t: ('center', max(w/30,int(w-0.5*w*t)))).set_duration(2.5).set_start(0.5).crossfadein(0.5)

logo_mov = logo.set_position( lambda t: ('center', max(w/30, min(w/2.5,int(w-0.5*w*t))))).set_duration(3).set_start(0.5).crossfadein(0.75)

# A CLIP WITH A TEXT AND A BLACK SEMI-OPAQUE BACKGROUND

text = TextClip(" ", font='Amiri-regular',
	               color='white', bg_color="purple", fontsize=30, size=(640,480))

txt = TextClip("Welcome to", font='Helvetica',color='white', fontsize=32, size=(180,40))
stxt = TextClip("The House of Your Dreams", font='Helvetica',color='white', fontsize=40, size=(480,40)).set_pos((80, 600)).set_duration(1).set_start(1.5).crossfadein(0.75)
# tex1 = TextClip("3 BHK Independent Floor", font='Amiri-regular', color='white', fontsize=50, interline=9).set_duration(DURATION).set_start(0).set_position('center', -100).crossfadein(.4)
txt1 = TextClip("3 BHK Independent Floor", font=bold_font, color='white', fontsize=50, interline=9).set_duration(3).set_start(0).set_pos(('center', 160)).crossfadein(.3)
txt_1 = TextClip("Unfurnished | 2250 sq.ft", font=bold_font, color='white', fontsize=40, interline=9).set_duration(2).set_start(1).set_pos(('center', 260)).crossfadein(.3)
stxt_1 = TextClip("DLF City II, DLF Phase 2, Gurgaon", font=plain_font, color='white', fontsize=30, interline=9).set_duration(1.5).set_start(1.5).set_pos(('center', 360)).crossfadein(.3)

txt_col = txt.on_color(size=(txt.w+60,txt.h+20),
                  color=(105,14,200), pos=('center','center'), col_opacity=0.87)


# THE TEXT CLIP IS ANIMATED.
# I am *NOT* explaining the formula, understands who can/want.
# txt_mov = txt_col.set_pos( lambda t: (max(w/30,int(w-0.5*w*t)), max(5*h/6,int(100*t))) )

txt_mov = txt_col.set_pos( lambda t: (max(w/16,int(w-0.5*w*t*t*t)), max(520,int(100*t))) ).set_duration(2).set_start(0.5).crossfadein(0.75)



# FINAL ASSEMBLY
final = CompositeVideoClip([background, txt_mov, stxt], size=VIDEO_SIZE).set_duration(DURATION)
# final = CompositeVideoClip([background, logo_mov], size=VIDEO_SIZE).set_duration(DURATION)
final.write_videofile("backgroundd.mp4",fps=60)