from config import client, model
import json

def detect_viral_clips(transcript_text):
    prompt=f"""

    Analyze this transcript

    find 5 viral reel moments.

    --> RULES:
    1- each reel should be 30-60 seconds
    2- choose moments that would likely perform well on TikTok/Shorts/Reels

    and for each moment you will:

    1- provide a hook title.
    2- caption
    3-suggested b-roll
    4-provide start timestamp
    5- provide end timestamp
    6-why it may go viral

    return only a valid json 
    transcript:
    {transcript_text}
    """

    response= client.models.generate_content(
        model= model,
        contents= prompt
    )
    print("RAW RESPONSE:")
    print(response.text)

    viral_clips=response.text

    viral_clips = viral_clips.replace("```json", "")
    viral_clips = viral_clips.replace("```", "")
    viral_clips = viral_clips.strip()
    viral_clips = json.loads(viral_clips)

    print("TYPE:", type(viral_clips))
    print("DATA:", viral_clips)

    return viral_clips

