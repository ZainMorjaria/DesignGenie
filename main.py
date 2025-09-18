from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import openai

# Create the app
app = FastAPI()

# CORS lets your frontend talk to your backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Your OpenAI API key
openai.api_key = "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"
# Route to generate text
@app.get("/generate")
def generate(prompt: str):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or use gpt-3.5-turbo if you prefer
        messages=[
            {"role": "user", "content": f"Turn this idea into a polished creative concept: {prompt}"}
        ]
    )
    return {"result": response["choices"][0]["message"]["content"]}

@app.get("/generate-image")
def generate_image(prompt: str):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"  # You can also use 256x256 or 1024x1024
    )
    return {"image_url": response["data"][0]["url"]}