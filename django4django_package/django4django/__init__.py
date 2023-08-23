from pathlib import Path
import os

app_version = "0.0.1"
BASE_DIR = Path(__file__).resolve().parent

with open(f"{BASE_DIR}/version.txt") as version:
    app_version = version.read()

VERSION = app_version