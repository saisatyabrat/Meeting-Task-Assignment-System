import whisper
import tempfile

def convert_audio_to_text(audio_file):
    model = whisper.load_model("base")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        temp_audio.write(audio_file.read())
        temp_audio.flush()
        result = model.transcribe(temp_audio.name)
    return result["text"]