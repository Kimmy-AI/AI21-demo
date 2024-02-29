import os
from ai21 import AI21Client
from ai21.models import ImprovementType

client = AI21Client(
    # This is the default and can be omitted
    api_key=os.environ.get("AI21_API_KEY"),
)

text = "Affiliated with the profession of project management, I have ameliorated myself with a different set of hard skills as well as soft skills."
response = client.improvements.create(
    text=text,
    types=[ImprovementType.FLUENCY],
)

print(response)
# Use the improvements suggestions to fix the sentence
improved_text = text
improvements = response.improvements
for curr_improvement in reversed(improvements):
    improved_text = (
        improved_text[: curr_improvement.start_index]
        + curr_improvement.suggestions[0]
        + improved_text[curr_improvement.end_index :]
    )

print(improved_text)
