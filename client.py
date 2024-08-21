from openai import OpenAI
client = OpenAI(
    api_key="your own api key"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "what is python programming"}
  ]
)

print(completion.choices[0].message)
