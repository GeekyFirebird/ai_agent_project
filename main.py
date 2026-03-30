import os
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    # Parser at the beggining for a fail test, make sure a prompt is passed in
    parser = argparse.ArgumentParser(description="Chatbot") #Creates a parser object
    parser.add_argument("user_prompt", type=str, help="User Prompt") # Adds an argument to the parser object
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args() # Reads the input from the command line and stores it in `args`

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("No api_key found")

    client = genai.Client(api_key=api_key)

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    generate_content(client, messages, args.verbose)


def generate_content(client, messages, verbose):

    response = client.models.generate_content(
        model = 'gemini-2.5-flash',
        contents = messages
    )

    response_metadata = response.usage_metadata

    if response_metadata is None:
        raise RuntimeError("No metadata available")

  
    if verbose:
        print("Prompt tokens:", response_metadata.prompt_token_count) 
        print("Response tokens:", response_metadata.candidates_token_count)

    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()