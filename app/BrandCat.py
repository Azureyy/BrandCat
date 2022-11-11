
import os
import openai
import argparse
import re
from typing import List

MAX_INPUT_LENGTH = 32

def main():
  print("Running BrandCat")
  parser = argparse.ArgumentParser()
  parser.add_argument("--input", "-i", type = str, required = True)
  args = parser.parse_args()
  user_input = args.input
  print(f"User input: {user_input}")
  if(validate(user_input)):
    generate_branding_snippet(user_input)
    generate_keywords(user_input)

  else:
    raise ValueError(f"Input length is too long. Must be under {MAX_INPUT_LENGTH}. Subimitted input is {user_input}")

def validate(prompt:str) -> bool:
  return len(prompt) <= MAX_INPUT_LENGTH


def generate_keywords(prompt: str) ->  str:
  # load API keys
  openai.api_key = "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"
  enriched_prompt = f"Generate branding keywords for {prompt}"
  print(enriched_prompt)
  response = openai.Completion.create(
    model="text-davinci-002",
    prompt=enriched_prompt,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0

  )

  # Extract text
  keywords_text:str = response["choices"][0]["text"]
  print(keywords_text)
  # Strip white space and split the keywords one by one
  keywords_text = keywords_text.strip()
  keywords__array = re.split(", |\n|;", keywords_text)
  
  keywords__array = [k for k in keywords__array if len(k) >0]

  print(f"keywords: {keywords__array}")

  return keywords__array

  
def generate_branding_snippet(prompt: str) -> str:
  # load API keys
  openai.api_key = "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"
  enriched_prompt = f"Generate branding snippet for {prompt}"
  print(enriched_prompt)
  response = openai.Completion.create(
    model="text-davinci-002",
    prompt=enriched_prompt,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  # Extract text
  branding_text:str = response["choices"][0]["text"]
  # Strip white space
  branding_text = branding_text.strip()

  print(f"snippet: {branding_text}")
  return branding_text


if __name__  == "__main__":
  main()