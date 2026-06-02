
from moviepy.video.io.VideoFileClip import VideoFileClip
def make_reels_verticals(reel_metadata):



    updated_reels=[]
    for reel in reel_metadata:

        video_path=reel['path']

        video=VideoFileClip(video_path)
        resized_video =video.resized(height=1920)

        x_center=resized_video.w/2
        vertical=resized_video.cropped(
            x1=x_center -540,
            x2=x_center+540,
            y1=0,
            y2=1920
        )
        vertical_path=video_path.replace('generated_clips','vertical_reels')
        vertical.write_videofile(
            vertical_path,
            codec="libx264",
            audio_codec="aac"
        )
        reel['path']=vertical_path
        updated_reels.append(reel)
    return updated_reels


