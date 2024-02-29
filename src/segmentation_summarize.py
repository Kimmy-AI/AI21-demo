import os
from ai21 import AI21Client
from ai21.models import DocumentType

client = AI21Client(
    # This is the default and can be omitted
    api_key=os.environ.get("AI21_API_KEY"),
)

res = client.segmentation.create(
    source="https://en.wikipedia.org/wiki/A",
    source_type=DocumentType.URL,
)

L = []
for curr_segment in res.segments:
    if curr_segment.segment_text and len(curr_segment.segment_text) >= 1000:
        try:
            res = client.summarize.create(
                source=curr_segment.segment_text,
                source_type=DocumentType.TEXT,
            )
            L.append(res.summary)
        except Exception as e:
            print(e)

print(L)
