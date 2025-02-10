from transformers import pipeline
from transformers import logging

logging.set_verbosity_error()

generator = pipeline("text-generation", model="distilgpt2")

if __name__ == "__main__":
    print("AI Emotion Chatbot (Type 'exit' to quit)")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break
        response = generator("User: " + user_input + "\nAI:", max_length=50, num_return_sequences=1)
        generated_text = response[0]["generated_text"]
        ai_response = generated_text[len("User: " + user_input):].strip()
        print(ai_response)
