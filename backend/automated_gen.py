from google import genai
from config import config

Api_key = config.get('Api_key')

def generate_code(prompt):
    client = genai.Client(api_key=Api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return response.text

