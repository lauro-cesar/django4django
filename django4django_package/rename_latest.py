import os 
import sys
import shutil

from pkg_resources import parse_version

with open("django4django/version.txt") as version:
    app_version=version.read()

v = parse_version(app_version)

micro=v.micro
minor=v.minor
major =v.major

sources = [{
    "in":f"dist/django4django-{v}.tar.gz",
    "out":f"dist/django4django-latest.tar.gz"
},
{
    "in":f"dist/django4django-{v}-py3-none-any.whl",
    "out":f"dist/django4django-latest-py3-none-any.whl"
}
]


for source in sources:
    filein = source.get("in")
    fileout = source.get("out")
    print(f"Movendo {filein} -> {fileout}")
    dest = shutil.copyfile(source.get("in"), source.get("out"))