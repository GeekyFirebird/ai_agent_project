import os
import argparse

from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("No api_key found")


    client = genai.Client(api_key=api_key)

    # prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    parser = argparse.ArgumentParser(description="Chatbot") #Creates a parser object
    parser.add_argument("user_prompt", type=str, help="User Prompt") # Adds an argument to the parser object
    args = parser.parse_args() # Reads the input from the command line and stores it in `args`

    response = client.models.generate_content(
        model = 'gemini-2.5-flash',
        contents = args.user_prompt
    )

    response_metadata = response.usage_metadata

    if response_metadata is None:
        raise RuntimeError("No metadata available")

    print("User prompt:", args.user_prompt)
    print("Prompt tokens:", response_metadata.prompt_token_count) 
    print("Response tokens:", response_metadata.candidates_token_count)
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()