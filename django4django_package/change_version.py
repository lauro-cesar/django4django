import os 
from pkg_resources import parse_version

app_version="0.0.1"

with open("django4django/version.txt") as version:
    app_version=version.read()

v = parse_version(app_version)

micro=v.micro
minor=v.minor
major =v.major


if micro < 1000:
    micro = micro+1

if micro >=999:
    micro=0
    minor = minor+1

if minor >=999:
    minor=0
    major= major+1

with open("django4django/version.txt","w") as version:
    version.write(f"{major}.{minor}.{micro}")