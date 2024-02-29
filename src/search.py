import os
from ai21 import AI21Client

client = AI21Client(
    # This is the default and can be omitted
    api_key=os.environ.get("AI21_API_KEY"),
)

try:
    cwd = os.getcwd()
    file_path = f"{cwd}/data/koala.txt"
    client.library.files.create(
        file_path=file_path,
        public_url="https://en.wikipedia.org/wiki/Koala",
    )
except Exception as e:
    print(e, "\n")

response = client.library.search.create(query="What is Koala?")
print(response)

print("\n")

response = client.library.search.create(query="How to train a custom model?")
print(response)
