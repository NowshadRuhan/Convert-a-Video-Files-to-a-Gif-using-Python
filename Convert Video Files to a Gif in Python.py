from moviepy.editor import VideoFileClip #pip3 install moviepy
from IPython.display import Image


videoClip = VideoFileClip("video1.mp4")
videoClip.write_gif("video1.gif")
![SegmentLocal](video1.gif "segment")
Image(url='video1.gif')  