import os
from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("No API key was found")
elif not api_key.startswith("sk-proj-"):
    print("An API key was found, but it doesn't start 'sk-proj-'")
else:
    print("Api key was found and looks good")
