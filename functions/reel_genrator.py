import json

from moviepy.video.io.VideoFileClip import VideoFileClip

with open("../outputs/reels/viral_clips.json","r") as f :
    data=json.load(f)

clips=data

full_video= VideoFileClip("../input_videos/The Calhoun Effect.mp4")
def timestamp_to_seconds(timestamp):

    minutes, seconds = timestamp.split(":")

    return int(minutes) * 60 + int(seconds)

reel_metadata=[]

for i, clip_data in enumerate(clips):
    start = timestamp_to_seconds(
        clip_data["start_timestamp"]
    )

    end = min(
        timestamp_to_seconds(
            clip_data["end_timestamp"]
        ),
        full_video.duration
    )


    reel=full_video.subclipped(start,end)
    reel_file=f"reel{i+1}"
    output_path=f"../outputs/generated_clips/{reel_file}.mp4"

    reel.write_videofile(
        output_path,
        codec='libx264',
        audio_codec='aac',
    )

    reel_metadata.append(
        {
            "reel_file":reel_file,
            'start': start,
            'end': end,
            "hook_title": clip_data["hook_title"]
        }
    )
with open("../outputs/reel_metadata/reel_metadata.json","w") as f:
    json.dump(reel_metadata, f, indent=4)
print("reels generated")
