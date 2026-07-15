import os
import tempfile
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


def convert_audio_to_text(audio_bytes):
    if not audio_bytes:
        return ""

    try:
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as temp_audio:
            temp_audio.write(audio_bytes)
            temp_audio_path = temp_audio.name

        with open(temp_audio_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                file=audio_file,
                model="whisper-large-v3",
                response_format="text"
            )

        return transcription.strip()

    except Exception as e:
        return f"Speech-to-text error: {str(e)}"