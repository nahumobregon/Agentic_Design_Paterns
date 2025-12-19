import json
import sys

filename = "Chapter 1_ Prompt Chaining (Code Example).ipynb"

try:
    with open(filename, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    print(f"Successfully loaded {filename}. It is valid JSON.")
    if 'cells' in nb and 'metadata' in nb:
        print("Structure looks like a notebook (has 'cells' and 'metadata').")
    else:
        print("Warning: JSON valid but missing 'cells' or 'metadata' keys.")
except Exception as e:
    print(f"Error loading {filename}: {e}")
