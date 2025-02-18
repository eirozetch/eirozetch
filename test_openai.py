from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);