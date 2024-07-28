from openai import OpenAI

client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="sk-proj-MYzWe2zVkgSnNP1iYI3nT3BlbkFJqBP6ZWunZG21uHSaUysT",
)
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a Virtual assistant named Jarvis, skilled in general tasks Alexa and Google cloud."},
    {"role": "user", "content": "What is coding"}
  ]
)

print(completion.choices[0].message)