import os
from ai21 import AI21Client

client = AI21Client(
    # This is the default and can be omitted
    api_key=os.environ.get("AI21_API_KEY"),
)

text = "jazzz is a great stile of music"
response = client.gec.create(text=text)

#  Use the corrections to fix the sentence
corrected_text = text
corrections = response.corrections
for curr_correction in reversed(corrections):
    corrected_text = (
        corrected_text[: curr_correction.start_index]
        + curr_correction.suggestion
        + corrected_text[curr_correction.end_index :]
    )

print(corrected_text)

