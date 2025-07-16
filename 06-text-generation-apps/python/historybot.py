import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key = os.environ['AZURE_OPENAI_API_KEY'],
    api_version = "2024-02-01"
)

deployment = os.environ['AZURE_OPENAI_DEPLOYMENT']

figure = input("What historical figure do you want to talk to?")
question = input("What topic would you like to learn about?")
prompt = f"Greetings {figure}, tell me about the following topic in your point of view: {question}. Ensure that your response doesn't exceed 200 words."

messages = [{"role": "system", "content": f"You are an AI history assistant taking the role of {figure}"},
            {"role": "user", "content": prompt}]

completion = client.chat.completions.create(model = deployment, messages = messages, temperature=0.2)
print(completion.choices[0].message.content)