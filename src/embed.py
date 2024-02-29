import os
from ai21 import AI21Client
from ai21.models import EmbedType

client = AI21Client(
    # This is the default and can be omitted
    api_key=os.environ.get("AI21_API_KEY"),
)

response = client.embed.create(
    texts=["You can now use AI21 Embeddings."],
    type=EmbedType.SEGMENT,
)

print(response)
