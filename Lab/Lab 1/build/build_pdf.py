"""Print the three Lab 1 HTML sources from Chrome."""
from pathlib import Path
import os
import webbrowser

BUILD = Path(__file__).resolve().parent
for name, layout in (
    ("requirements-table", "landscape"),
    ("uml-use-case", "landscape"),
    ("use-case-flow", "portrait"),
):
    print(f"Open {name}.html, print in {layout}, and save as PDF in submission/.")
    webbrowser.open((BUILD / f"{name}.html").as_uri())
