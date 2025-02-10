from dotenv import load_dotenv
import os
import openai

load_dotenv(override=True)

def detect_emotion(user_input):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = f"Analyze the emotion of this text: \"{user_input}\". Reply with one emotion depend on 6 basic emotions."

    response = openai.ChatCompletion.create(
        model=os.getenv("MODEL_NAME"),
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"].strip()
