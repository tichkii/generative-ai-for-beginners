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

recipes = input("State the amount of recipes to generate (e.g 2): ")
ingredients = input("State the available ingredients (e.g Chicken, Eggs, Potatoes)")
filters = input("State any special dietary requirements (e.g Halal, Vegan, Gluten-free)")

prompt = f""" Generate : [{recipes}] recipes,
With the following available ingredients : [{ingredients}],
Suitable for people that follow [{filters}] dietary restrictions.
Include a shopping list at the end of each recipe for ingredients that are missing but are crucial for the recipe. Make sure that the recipes focus more on what is available than what is missing.
"""
messages = [{"role": "user", "content": prompt}]

completion = client.chat.completions.create(model=deployment, messages = messages)

print(completion.choices[0].message.content)

