import os
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-small-latest"
# "DHIkLF0GB6Y9mEcoCrK3tLD6W7gHsI0S"
client = Mistral(api_key=api_key)
print("API KEY:", api_key)
chat_response = client.chat.complete(
    model=model,
    messages=[
        {
            "role": "user",
            "content": "Loops syntax in Python with examples",
        },
    ],
    temperature = 1, # Increasing randomness and diversity of the output, this is required to be higher than 0 to have diverse outputs
    n = 10 # Number of completions
)

for i, choice in enumerate(chat_response.choices):
    print(choice.message.content)