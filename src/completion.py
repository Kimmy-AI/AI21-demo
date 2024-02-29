import os
from ai21 import AI21Client

client = AI21Client(
    # This is the default and can be omitted
    api_key=os.environ.get("AI21_API_KEY"),
)

res = client.completion.create(
    model="j2-ultra",
    prompt="Write a product title for a sports T-shirt to be published on an online retail platform. Include the following keywords: activewear, gym, dryfit.",
    temperature=0.8,
    max_tokens=200,
)

print(res)
