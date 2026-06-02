
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip


def add_captions(transcript,reel_metadata):




    captions=[]

    for reel_info in reel_metadata:
        reel_file=reel_info["reel_file"]
        reel_start=reel_info["start"]
        reel_end=reel_info["end"]

        print(f"preprocessing {reel_file}")

        video_path = reel_info['path']

        video = VideoFileClip(video_path)

        subtitle_4clips = []

        filtered_segments=[]

        for segment in transcript:
            if (
                segment['start']>= reel_start
                    and
                segment['end']<= reel_end
                ):
                filtered_segments.append(segment)

        for segment in filtered_segments:
            text=segment['text']
            start_time=segment['start']-reel_start
            end_time=segment['end']-reel_start

            txt_clip=TextClip(
                text=text,
                font_size=70,
                color="white",
                stroke_color="black",
                stroke_width=2,
                size=(int(video.w * 0.9), None),
                method="caption"
            )

            txt_clip=(
                txt_clip
                .with_position(("center",video.h * 0.75))
                .with_start(start_time)
                .with_end(end_time)
            )
            subtitle_4clips.append(txt_clip)


        final_reel=CompositeVideoClip(
            [video]+subtitle_4clips,
        )

        output_path=reel_info['path'].replace(
            'vertical_reels',
            'captions'
        )
        final_reel.write_videofile(
            output_path,
            codec="libx264",
            audio_codec="aac"
        )

        reel_info['path']=output_path
        captions.append(reel_info)
    return captions