import os
from dotenv import load_dotenv

load_dotenv()

def get_google_api_key():
    return os.getenv("GOOGLE_API_KEY")

def get_huggingface_api_key():
    return os.getenv("HF_API_KEY")
