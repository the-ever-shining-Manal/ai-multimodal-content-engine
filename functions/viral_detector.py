from config import client, model
import json
import os

with open ("../outputs/transcripts/transcript_text_and_timestamps.json","r",encoding='utf-8') as f:
    transcript_text = json.load(f)

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

viral_clips=response.text

viral_clips = viral_clips.replace("```json", "")
viral_clips = viral_clips.replace("```", "")
viral_clips = viral_clips.strip()
viral_clips_json = json.loads(viral_clips)
print(viral_clips)
with open("../outputs/reels/viral_clips.json","w",encoding='utf-8') as f:
    json.dump(viral_clips_json,f,indent=4)

    print("viral clips saved!!")