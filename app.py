from fastapi import FastAPI
from pydantic import BaseModel
from utils.emotion_detector import detect_emotion
from utils.response_generator import generate_response

if __name__ == "__main__":
    print("AI Emotion Chatbot (Type 'exit' to quit)")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break
        emotion = detect_emotion(user_input)
        reply = generate_response(user_input, emotion)
        print(f"AI ({emotion}): {reply}")

app = FastAPI()

class MessageRequest(BaseModel):
    user_input: str

@app.post("/api/emotion-chatbot")
async def chat(request: MessageRequest):
    emotion = detect_emotion(request.user_input)
    reply = generate_response(request.user_input, emotion)
    return {"emtion": emotion, "reply": reply}