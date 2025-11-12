# import openai

# openai.api_key = "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"


import google.generativeai as genai

genai.configure(api_key="Enter API key")

def chat_with_gemini(prompt):
    model = genai.GenerativeModel("gemini-pro-latest")  # or gemini-flash-latest or your listed model name
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = chat_with_gemini(user_input)
        print("Gemini:", response)



