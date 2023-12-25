from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "what does the name krishiv mean."},
  ]
)

print(completion.choices[0].message)