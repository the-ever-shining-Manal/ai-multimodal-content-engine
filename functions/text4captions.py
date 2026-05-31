import whisper
import json
model=whisper.load_model("base")

results=model.transcribe(r"../input_videos/The Calhoun Effect.mp4",
                         word_timestamps=True)

segments=results["segments"]

with open("../outputs/transcripts/test4captions.json",'w',encoding='utf-8') as f:
    json.dump(segments,f,indent=4,ensure_ascii=False)
