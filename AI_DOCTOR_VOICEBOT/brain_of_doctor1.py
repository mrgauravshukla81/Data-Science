#step 1 :setup groq api
import os
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
#step 2:covert image to required format
import base64
image_path="acne.jpg.webp"
image_file=open(image_path,"rb")
base64_image=base64.b64encode(image_file.read()).decode("utf-8")
#step 3 step multilevel LLM
from groq import Groq
client=Groq()
query="is somthing wrong with my face"
model="llama-3.3-70b-versatile"
messages=[
    {
        "role": "user",
        "content": [
         {
          "type":"text"
          "text": query
         },
         {
          "type":"image_url"
          "image_url":{
            "url":f"data:image/jpeg;base64,{base64_image}",
          },
         },
        ],
    },]
chat_completion=client.chat.completions.create(
    messages=messages,
    model=model
)
   print(chat_completion)