import socket
import google.generativeai as genai
from PIL import Image

# Local
from constants import POEM_INSTRUCTIONS_PROMPT
__current_system_hostname__ = socket.gethostname()

# Function to call the Gemini LLM API (you'll need to replace with actual API details)
def get_poem_from_image(image: Image, gemini_model: genai.GenerativeModel) -> str:
    response = gemini_model.generate_content([
        POEM_INSTRUCTIONS_PROMPT,
        image,
    ])
    response.resolve()
    return response.text