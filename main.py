import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Key not found")

    client = genai.Client(api_key=api_key)

    # messages:  list[types.Content] = [
    #     types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
    # ]
    

    # prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=args.user_prompt
    )

    if not response.usage_metadata:
        raise RuntimeError("No metadata available")

    prompt_tokens = response.usage_metadata.prompt_token_count #shows the number of tokens in the prompt that was sent to the model
    response_tokens = response.usage_metadata.candidates_token_count #shows the number of tokens in the model's response



    print(f"""
        User prompt: {args.user_prompt}
        Prompt tokens: {prompt_tokens}
        Response tokens: {response_tokens}
        Response: {response.text}
    """)


if __name__ == "__main__":
    main()

