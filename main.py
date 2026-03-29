import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("No api_key found")


client = genai.Client(api_key=api_key)

prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

response = client.models.generate_content(
    model = 'gemini-2.5-flash',
    contents = prompt
)

response_metadata = response.usage_metadata

print(f"User Prompt: {prompt}")

if response_metadata is None:
    raise RuntimeError("No metadata available")
else:
    print(f"""
          Prompt Tokens: {response_metadata.prompt_token_count}\n 
          Response Tokens: {response_metadata.candidates_token_count}
    """)

print(f"Response: {response.text}")
