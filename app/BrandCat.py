import os
import openai

openai.api_key = "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"
subject = "coffee"
prompt = f"Generate branding snippet for {subject}"

response = openai.Completion.create(
  model="text-davinci-002",
  prompt=prompt,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)