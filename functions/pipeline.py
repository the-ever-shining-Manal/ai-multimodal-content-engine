from functions.transcribe import transcribe
from functions.viral_detector import detect_viral_clips
from functions.reel_genrator import generate_reels
from functions.make_reels_verticals import make_reels_verticals
from functions.caption_generator import add_captions


def process_video(video_path):

    print("1. Transcribing...")

    transcript = transcribe(
        video_path
    )

    print("2. Detecting viral moments...")

    viral_data = detect_viral_clips(
        transcript
    )
    print(type(viral_data))
    print(viral_data)
    if isinstance(viral_data, dict):
        clips = viral_data.get("viral_reels") or viral_data.get("viral_reel_moments") or viral_data.get("reels") or []
    else:
        clips = viral_data

    print("3. Generating reels...")

    reels = generate_reels(
        video_path,
        clips
    )

    print("4. Making vertical reels...")

    reels = make_reels_verticals(
        reels
    )

    print("5. Adding captions...")

    reels = add_captions(
        transcript,
        reels
    )



    return {
        "reels": reels,
        "viral_clips": clips
    }