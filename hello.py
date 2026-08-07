# print("Hello Ashiq!")
# print("My AI journey starts today")
# import openai

# print("OpenAI SDK installed successfully")

# text = "I am learning how LLMs work"
# tokens = text.split()
# print("Tokens:")
# for token in tokens:
#     print(token)


# #----------------------------
# predictions = {
#     "I love": "Python",
#     "Python is": "awesome",
#     "AI will": "transform"
# }

# prompt = input("Enter phrase: ")

# print(
#     predictions.get(
#         prompt,
#         "I cannot predict"
#     )
# )

#  Temperature Demonstration 
import random

responses = [
    "AI is fascinating.",
    "AI is transforming industries.",
    "AI helps automate tasks.",
    "AI enables new applications."
]

print(random.choice(responses))

# LLM Call (OpenAI)

from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "Explain transformers simply"
        }
    ]
)

print(
    response.choices[0].message.content
)

