import openai
from config import *
from utils import *



openai.api_key = API_KEY

def get_ai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content'].strip()

def main():
    print("Chatbot: Hello! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        cleaned_input = clean_text(user_input)
        response = get_ai_response(cleaned_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()


