

from moviepy.video.io.VideoFileClip import VideoFileClip



def timestamp_to_seconds(timestamp):
    if isinstance(timestamp, (int,float)):
        return float(timestamp)
    minutes, seconds = timestamp.split(":")

    return int(minutes) * 60 + int(seconds)


def generate_reels(video_path,clips):
    full_video=VideoFileClip(video_path)

    reel_metadata = []
    print(type(clips))
    print(clips)
    for i, clip_data in enumerate(clips):
        """"
        start = timestamp_to_seconds(
            clip_data["start_timestamp"]
        )

        end = min(
            timestamp_to_seconds(
            clip_data["end_timestamp"]
            ),
            full_video.duration
        )
"""
        start = float(clip_data["start_timestamp"])
        end= min(float(clip_data["end_timestamp"]), full_video.duration)
        reel = full_video.subclipped(start, end)
        reel_file = f"reel{i + 1}"
        output_path = f"outputs/generated_clips/{reel_file}.mp4"

        reel.write_videofile(
            output_path,
            codec='libx264',
            audio_codec='aac',
        )

        reel_metadata.append(
            {
                "reel_file": reel_file,
                'start': start,
                'end': end,
                "hook_title": clip_data["hook_title"],
                'path': output_path,

            }
        )
    return reel_metadata

