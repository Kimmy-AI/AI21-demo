import os
from ai21 import AI21Client

client = AI21Client(
    # This is the default and can be omitted
    api_key=os.environ.get("AI21_API_KEY"),
)

res = client.paraphrase.create(
    text="My team discovered that there was little-to-no information that answered the question, “Is my contractor licensed?” We figured that we should create some pages that satisfied this need.",
    start_index=116,
)

print(res)
