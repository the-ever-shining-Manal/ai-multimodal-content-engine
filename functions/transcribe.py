import whisper

def transcribe(video_path):
    model=whisper.load_model("base")

    results=model.transcribe(video_path,word_timestamps=True)
    clean_segments=[]
    for segment in results['segments']:
        clean_segments.append(
            {
                'start': segment['start'],
                'end': segment['end'],
                'text': segment['text'],
                'words':segment.get('words')
            }
        )
    return clean_segments

