import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx.Resize import Resize
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

input_folder='../outputs/generated_clips'
output_folder='../outputs/vertical_reels'

for file in os.listdir(input_folder):
    print(f"processing {file}")
    video_path=os.path.join(input_folder,file)

    video=VideoFileClip(video_path)
    resized_video =video.resized(height=1920)

    x_center=resized_video.w/2
    vertical=resized_video.cropped(
        x1=x_center -540,
        x2=x_center+540,
        y1=0,
        y2=1920
    )

    output_path=os.path.join(output_folder,f"{file}")
    vertical.write_videofile(output_path,codec='libx264',audio_codec='aac')
    print(f"finished processing {file}")
