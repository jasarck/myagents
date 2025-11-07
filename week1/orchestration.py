import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import Markdown, display

load_dotenv(override=True)

perplexity_api_key = os.getenv('PERPLEXITY_API_KEY')
google_api_key=os.getenv('GOOGLE_API_KEY')


if perplexity_api_key:
    print(f"Perplexity API Key exists and begins {perplexity_api_key[:8]}")
else:
    print("Perplexity API Key not set")

if google_api_key:
    print(f"Gemini API Key exists and begins {google_api_key[:8]}")
else:
    print("Gemini API Key not set")

request = "Please come up with a challenging, nuanced question that I can ask a number of LLMs to evaluate their intelligence. "
request += "Answer only with the question, no explanation."
messages = [{"role": "user", "content": request}]


messages

perplexityai = OpenAI(api_key=perplexity_api_key, base_url="https://api.perplexity.ai")
googleai = OpenAI(api_key=google_api_key,base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

MODEL = "sonar"
response = perplexityai.chat.completions.create(
    model=MODEL,
    messages=messages
)

question = response.choices[0].message.content
print("***************question**************")
print(question)

competitors = []
answers = []
messages = [{"role": "user", "content": question}]

MODEL = "sonar"
response = perplexityai.chat.completions.create(
    model=MODEL,
    messages=messages
)
print("***************Answer Perplexity**************")
answer = response.choices[0].message.content
print(answer)

competitors.append(MODEL)
answers.append(answer)

MODEL = "gemini-2.0-flash"
response = googleai.chat.completions.create(
    model=MODEL, # Use a compatible Gemini model name
    messages=messages
)

answer = response.choices[0].message.content
print("***************Answer Gemini**************")
print(answer)
competitors.append(MODEL)
answers.append(answer)


for competitor, answer in zip(competitors, answers):
    print(f"Competitor: {competitor}\n\n{answer}")


together = ""
for index, answer in enumerate(answers):
    together += f"# Response from competitor {index+1}\n\n"
    together += answer + "\n\n"



judge = f"""You are judging a competition between {len(competitors)} competitors.
Each model has been given this question:

{question}

Your job is to evaluate each response for clarity and strength of argument, and rank them in order of best to worst.
Respond with JSON, and only JSON, with the following format:
{{"results": ["best competitor number", "second best competitor number", "third best competitor number", ...]}}

Here are the responses from each competitor:

{together}

Now respond with the JSON with the ranked order of the competitors, nothing else. Do not include markdown formatting or code blocks."""


judge_messages = [{"role": "user", "content": judge}]

MODEL = "gemini-2.5-flash"
response = googleai.chat.completions.create(
    model=MODEL, # Use a compatible Gemini model name
    messages=judge_messages
)

results = response.choices[0].message.content

# OK let's turn this into results!

results_dict = json.loads(results)
ranks = results_dict["results"]
for index, result in enumerate(ranks):
    competitor = competitors[int(result)-1]
    print(f"Rank {index+1}: {competitor}")