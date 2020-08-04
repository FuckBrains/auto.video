from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, afx, transfx, concatenate, CompositeVideoClip, AudioFileClip, CompositeAudioClip
from config import *
from util import *

output = "video/"+VIDEO_SUB_PATH+"/slideshow.mp4"
clip0 = VideoFileClip("video/"+VIDEO_SUB_PATH+"/slide0.mp4")
# clip1 = VideoFileClip("video/"+VIDEO_SUB_PATH+"/slide1.mp4")
clip2 = VideoFileClip("video/"+VIDEO_SUB_PATH+"/slide2.mp4")
# clip3 = VideoFileClip("video/"+VIDEO_SUB_PATH+"/slide3.mp4")
clip4 = VideoFileClip("video/"+VIDEO_SUB_PATH+"/slide4.mp4")
clip5 = VideoFileClip("video/"+VIDEO_SUB_PATH+"/slide5.mp4")
clip6 = VideoFileClip("video/"+VIDEO_SUB_PATH+"/slide6.mp4")
clip7 = VideoFileClip("video/"+VIDEO_SUB_PATH+"/slide7.mp4")
# clip8 = VideoFileClip("video/"+VIDEO_SUB_PATH+"/slide6_1.mp4")
# clip9 = VideoFileClip("video/"+VIDEO_SUB_PATH+"/slide7_1.mp4")
# clip10 = VideoFileClip("video/"+VIDEO_SUB_PATH+"/slide8.mp4")
clip11 = VideoFileClip("video/"+VIDEO_SUB_PATH+"/slide10.mp4")

audio_background = AudioFileClip(BG_AUDIO)
final_audio = CompositeAudioClip([audio_background])

# slide1 = CompositeVideoClip([clip1.fx( transfx.crossfadein, delay)])
slide2 = CompositeVideoClip([clip2.fx( transfx.slide_in, delay, 'bottom')])
slide3 = CompositeVideoClip([clip11.fx( transfx.crossfadeout, 2)])
slide4 = CompositeVideoClip([clip4.fx( transfx.slide_out, delay, 'left')])
slide5 = CompositeVideoClip([clip5.fx( transfx.crossfadein, delay)])
slide6 = CompositeVideoClip([clip6.fx( transfx.crossfadein, delay)])
slide7 = CompositeVideoClip([clip7.fx( transfx.crossfadein, delay)])
# slide8 = CompositeVideoClip([clip8.fx( transfx.slide_in, delay, 'right')])
# slide9 = CompositeVideoClip([clip9.fx( transfx.crossfadein, delay)])
# slide10 = CompositeVideoClip([clip10.fx( transfx.crossfadein, delay)])
# slided_clips = concatenate([clip0, slide1, slide2, slide3, slide4, slide6, slide7, slide8, slide9, slide5], padding=-delay, method="compose")
# slided_clips = concatenate([clip0, slide1, slide2, slide6, slide7, slide8, slide9, slide10, slide4, slide3, slide5], padding=-delay, method="compose").set_audio(final_audio)
slided_clips = concatenate([clip0, slide2, slide6, slide7, slide4, slide3, slide5], padding=-delay, method="compose").set_audio(final_audio)

slided_clips.write_videofile(output)