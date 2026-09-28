import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "cases" / "case_01.md"
BASE = ROOT / "BASELINE_PROMPT.md"
GUARD = ROOT / "GUARDIAN_PROMPT.md"
OUT = ROOT / "generated"
OUT.mkdir(exist_ok=True)

case = CASE.read_text()
baseline = BASE.read_text() + "\n\n" + case
guardian = GUARD.read_text() + "\n\n" + case

items = [("baseline", baseline), ("guardian", guardian)]
random.shuffle(items)

for label, (condition, prompt) in zip(("A", "B"), items):
    (OUT / f"condition_{label}.md").write_text(prompt)

key = {label: condition for label, (condition, _) in zip(("A", "B"), items)}
(OUT / "answer_key.json").write_text(json.dumps(key, indent=2))

print("Generated condition_A.md, condition_B.md, and answer_key.json")
print("Do not open answer_key.json until scoring is complete.")
