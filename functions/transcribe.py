import whisper
import json
model=whisper.load_model("base")

results=model.transcribe(r"../input_videos/The Calhoun Effect.mp4")
clean_segments=[]
for segment in results['segments']:
    clean_segments.append(
        {
            'start': segment['start'],
            'end': segment['end'],
            'text': segment['text']
        }
    )


for segment in clean_segments:
    print(segment['start'],segment['text'])


with open("../outputs/transcripts/transcript_text_and_timestamps.json", "w", encoding='utf-8') as f:
    json.dump(clean_segments,f,indent=4)

print("transcript is done!!!")