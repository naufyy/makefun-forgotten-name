"""Entry for Roast Your Own Agent.

Writes the winning one-line roast to /output/entry.txt.
The roast is specific to how an AI agent actually behaves: it forgets
the user mid-sentence, then bills for the tokens spent forgetting.
"""

import os

TEXT = "My agent forgot my name mid-sentence, then charged me for the tokens it spent forgetting it."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
