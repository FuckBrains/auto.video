from __future__ import division
from config import *

VIDEO_PATH = "video/"+VIDEO_SUB_PATH+"/slide5"+name_suffix+".mp4"
BG_PATH = "asset/"+ASSET_SUB_PATH+"slide3.png"
OBJ_PATH = "asset/"+TEMPLATE_PATH+"logo.png"

background = ImageClip(BG_PATH). \
        set_position(('center', 'center'))

logo = ImageClip(OBJ_PATH). \
        set_position(('center', 'center')).resize(1/size_factor)

logo_mov = logo.set_position( lambda t: ('center', max(w/4, min(w/2.5,int(w-0.5*w*t))))).set_duration(DURATION - START_TIME).set_start(START_TIME).crossfadein(FADE_TIME)

# FINAL ASSEMBLY
final = CompositeVideoClip([background, logo_mov], size=VIDEO_SIZE).set_duration(DURATION)

final.write_videofile(VIDEO_PATH,fps=fps)