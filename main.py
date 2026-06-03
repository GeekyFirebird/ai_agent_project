import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

def main() -> None:
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Key not found")

    client = genai.Client(api_key=api_key)

    messages:  list[types.Content] = [
        types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
    ]

    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    generate_content(client, messages, args.verbose)
    

def generate_content(client: genai.Client, messages: list[types.Content], verbose: bool) -> None:

    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=messages
    )

    if not response.usage_metadata:
        raise RuntimeError("No metadata available")

    prompt_tokens = response.usage_metadata.prompt_token_count #shows the number of tokens in the prompt that was sent to the model
    response_tokens = response.usage_metadata.candidates_token_count #shows the number of tokens in the model's response

    if verbose:
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    print(f"Response:\n {response.text}")


if __name__ == "__main__":
    main()

