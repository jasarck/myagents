from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv(override=True)



perplexity_api_key = os.getenv('PERPLEXITY_API_KEY')
google_api_key=os.getenv('GOOGLE_API_KEY')
print(f'{perplexity_api_key[:8]}')

openai = OpenAI(api_key=perplexity_api_key, base_url="https://api.perplexity.ai")

googleai = OpenAI(api_key=google_api_key,base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
print(openai)
print(googleai)

print("-------------------PERPLEXITY----------------------")
messages = [{"role": "user", "content": "What is the capital of France?"}]
print(messages)

MODEL = "sonar"
response = openai.chat.completions.create(
    model=MODEL,
    messages=messages
)

print(response.choices[0].message.content)

print("-------------------GEMINI----------------------")
response = googleai.chat.completions.create(
    model="gemini-2.5-flash", # Use a compatible Gemini model name
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain to me how generative AI works"}
    ]
)

# print(response.choices[0].message.content)


# image = googleai.images.generate(
#     model="gemini-2.5-flash",
#     prompt="A cute robot reading a book under a tree"
# )
# print(image.data[0].url)