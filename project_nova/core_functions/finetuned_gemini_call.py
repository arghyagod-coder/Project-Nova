import os 
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()

genai.configure(api_key=os.environ["Gemini_key"])


def get_gemini(prompt:str, model:str="gemini-1.5-flash"):

    model = genai.GenerativeModel(model)
    response = model.generate_content(prompt)
    return response.text

