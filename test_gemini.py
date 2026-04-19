import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Load the environment variable from your .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# 2. Configure the library
genai.configure(api_key=api_key)

# 3. Initialize the model (Gemini 2.5 Flash is great for testing)
model = genai.GenerativeModel('gemini-2.5-flash')

# 4. Generate a response
response = model.generate_content("Give me a quick 'Hello World' from Gemini!")

print(response.text)