from openai import OpenAI
client = OpenAI(
    api_key="sk-None-5WvwlXJ5i3FWnU6c3ZldT3BlbkFJylLhG6NjQ3jwky5vkTdj"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "what is programming."}
  ]
)

print(completion.choices[0].message)
