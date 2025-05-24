import openai
import os

# Set your OpenAI API key here (or use dotenv)
openai.api_key = "YOUR_API_KEY"

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    input_text = input("Enter a prompt for the AI: ")
    result = generate_response(input_text)
    print("AI Response:\n", result)
