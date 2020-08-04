# from __future__ import division
from config import *
from util import *

VIDEO_PATH = "video/"+VIDEO_SUB_PATH+"/slide3"+name_suffix+".mp4"
BG_PATH = "asset/"+ASSET_SUB_PATH+"slide3.png"
DURATION = 8
background = ImageClip(BG_PATH). \
        set_position(('center', 'center'))

# A CLIP WITH A TEXT AND A BLACK SEMI-OPAQUE BACKGROUND

# txt = "This is a 1 BHK Fully Furnished Independent Floor available for rent. The property is on floor number 4 in a building with 4 floors. Property for rent available at unbeatable price in Raja Garden, check out now. Mid-segment homes for rent now in Delhi. Security charges of Rs 10000 is applicable. Monthly rent is Rs 10000. Contact for more information. If you are looking for about 200 sq ft (Carpet Area) property near your office, this is a perfect fit. Check out this 800 sq ft built up area property, available at an affordable rent. Top flooring in 0 bathrooms. Rental property available at affordable prices, check 0 pictures. It is available starting 2020-05-27. Very close to reputed schools such as Tiny Rosary School, Nigam Aadarsh Prathmik Vidyalaya, and Nigam adarsh prathmik vidhayala. This property is in walking distance from Kalra Hospital, Maharaja Agrasen Hospital, and Sri Balaji Action Medical Institute."
with open("asset/"+ASSET_SUB_PATH+"desc.txt", "r") as myfile:
  txt = myfile.read()
diff = len(txt) - DESCRIPTION_TEXT_COUNT
interline = 34

if len(txt) > 1:
	num_rows = diff / 70
	if num_rows < 4:
		font_size = font_size - 4/size_factor
		text_count = 80
		interline = 30
	elif num_rows < 8:
		font_size = font_size - 8/size_factor
		text_count = 100
		interline = 26
	else:
		font_size = font_size - 16/size_factor
		text_count = 150
		interline = 22

txt = insert_newlines(txt, text_count)

stxt = TextClip(txt, font=plain_font,color=font_color, fontsize=font_size, method='label', interline=interline/size_factor).set_pos(('center', 'center')).set_duration(DURATION - START_TIME).set_start(START_TIME).crossfadein(FADE_TIME)

# FINAL ASSEMBLY
final = CompositeVideoClip([background, stxt], size=VIDEO_SIZE).set_duration(DURATION)

final.write_videofile(VIDEO_PATH,fps=fps)


