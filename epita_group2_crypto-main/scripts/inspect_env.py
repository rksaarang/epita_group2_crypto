
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

# Load local environment configuration for inspection.
load_dotenv()

print("=== Python Environment Inspection ===")
print(f"Python executable : {sys.executable}")
print(f"Python version    : {sys.version}")
print(f"Virtual env prefix: {sys.prefix}")
print(f"Base prefix       : {sys.base_prefix}")
print(f"Inside virtual env: {sys.prefix != sys.base_prefix}")

print("\n=== API Key Configuration ===")
print(
    "CRYPTOCOMPARE_API_KEY configured:",
    bool(os.getenv("CRYPTOCOMPARE_API_KEY")),
)

print("\n=== PATH Entries ===")
for entry in os.environ.get("PATH", "").split(os.pathsep):
    print(entry)

print("\n=== Python Import Paths ===")
for entry in sys.path:
    print(entry)

print("\n=== Project Directory ===")
print(Path.cwd())
