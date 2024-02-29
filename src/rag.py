import os
from ai21 import AI21Client

client = AI21Client(
    # This is the default and can be omitted
    api_key=os.environ.get("AI21_API_KEY"),
)

try:
    cwd = os.getcwd()
    file_path = f"{cwd}/data/context.txt"
    client.library.files.create(file_path=file_path)
except Exception as e:
    print(e, "\n")

response = client.library.answer.create(question="How many examples do I need?")

if response.answer_in_context:
    print(response.answer)
else:
    print("The answer is not in the documents")


response = client.library.answer.create(
    question="What's my meal allowance when working from home?"
)

if response.answer_in_context:
    print(response.answer)
else:
    print("The answer is not in the documents")
