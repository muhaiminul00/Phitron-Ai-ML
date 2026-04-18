from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
import io
from gtts import gTTS

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def note_generator(images):
    
    prompt = """Summurize the picture in note format at 100 words max.
    Keep all markdown formats where neccessary in note."""
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt],
    )
    
    return response.text

def audio_generator(text):
    text = text.replace("#", "")
    text = text.replace("*", "")
    
    audio_buffer = io.BytesIO()
    speech = gTTS(text, lang='en', slow=False)
    speech.write_to_fp(audio_buffer)
    return audio_buffer

def quiz_generator(images, dificulties):
    
    prompt = f"Generate 3 quizzes based on {dificulties}. Keep all markdown formats where neccessary."
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt],
    )
    
    return response.text    