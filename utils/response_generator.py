from dotenv import load_dotenv
import os
import openai

load_dotenv(override=True)

def generate_response(user_input, emotion):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = f"You are a chatbot that responds with {emotion.lower()} tone. User: {user_input}"

    response = openai.ChatCompletion.create(
        model=os.getenv("MODEL_NAME"),
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"].strip()
