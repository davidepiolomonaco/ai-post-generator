import openai
from dotenv import load_dotenv
import os

def load_api_key():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    return api_key


def generate_post(article_title: str) -> str:
    openai.api_key = load_api_key()
    
    prompt = (
        f"Scrivi un post professionale per LinkedIn su questo articolo accademico:\n"
        f"Titolo: {article_title}\n"
        f"Il tono deve essere informativo e ispirazionale."
    )
    
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}],
        temperature = 0.5
    )
    
    return response.choices[0].message.content.strip()