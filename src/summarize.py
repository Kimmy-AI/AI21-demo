import os
from ai21 import AI21Client
from ai21.models import DocumentType

client = AI21Client(
    # This is the default and can be omitted
    api_key=os.environ.get("AI21_API_KEY")
)
res = client.summarize.create(
    source="""Rob Roussel, senior project manager, said the bioremediation process was successfully breaking down the oil into carbon dioxide and water. He said the process was at the mercy of the weather, but would hopefully be complete by the end of next month. The oil was dumped in the quarry in the Vale after the tanker spill in 1967.
The 974ft (297m) Torrey Canyon was carrying 100,000 tons of crude oil when it hit the UK's south-west coast.
The shipwreck coated miles of Cornish beach in brown sludge with the pollution stretching from Hartland Point in North Devon to the Channel Islands and even the coast of Normandy.

""",
    source_type=DocumentType.TEXT,
)

print(res)
