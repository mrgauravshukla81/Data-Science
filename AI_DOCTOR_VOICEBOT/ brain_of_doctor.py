# brain_of_doctor.py

# Optional: Load env vars if not using pipenv
from dotenv import load_dotenv
load_dotenv()

import os
import base64
from groq import Groq

# Step 1: Setup GROQ API Key
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in environment variables.")

client = Groq(api_key=GROQ_API_KEY)

# Step 2: Convert image to base64 format
def encode_image(image_path):   
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Step 3: Multimodal LLM query with image
def analyze_image_with_query(query, model, image_path):
    encoded_image = encode_image(image_path)
    
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}}
            ]
        }
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    return response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    image_path = "/Users/gauravshukla/Desktop/data science/python code/AI_DOCTOR_VOICEBOT/acne.jpg.webp"  # Ensure file exists
    query = "Is there something wrong with my face?"
    model = "meta-llama/llama-4-scout-17b-16e-instruct"  # Use the supported vision model
    
    result = analyze_image_with_query(query, model, image_path)
    print("🧠 Diagnosis:", result)
