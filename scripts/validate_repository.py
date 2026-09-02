from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
markdown_files = sorted(ROOT.rglob("*.md"))

assert (ROOT / "README.md").exists(), "README.md is required"
assert markdown_files, "No documentation was found"

missing: list[str] = []
for document in markdown_files:
    text = document.read_text(encoding="utf-8")
    assert "TODO" not in text, f"Unresolved TODO in {document.relative_to(ROOT)}"
    for target in re.findall(r"!?(?:\[[^\]]*\])\(([^)]+)\)", text):
        target = target.strip().split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        path = (document.parent / target).resolve()
        if not path.exists():
            missing.append(f"{document.relative_to(ROOT)} -> {target}")

if missing:
    raise SystemExit("Broken local references:\n" + "\n".join(missing))

readme = (ROOT / "README.md").read_text(encoding="utf-8")
for required in ("Project Objective", "MITRE ATT&CK", "Detection Validation"):
    assert required in readme, f"README is missing required section: {required}"

print(f"Validated {len(markdown_files)} Markdown files and their local evidence links.")
