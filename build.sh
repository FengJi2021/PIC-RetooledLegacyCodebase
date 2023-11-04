#!/bin/bash

# Exit on error
set -e

# Description: Make executable file for PIC
echo "Make executable file for PIC"

# make dir
mkdir -p build/dist
mkdir -p build/work

# build
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    pyinstaller --distpath=build/dist --workpath=build/work --name=PIC app/main.py
elif [[ "$OSTYPE" == "darwin"* ]]; then
    pyinstaller --distpath=build/dist --workpath=build/work --name=PIC app/main.py
elif [[ "$OSTYPE" == "msys"* ]] || [[ "$OSTYPE" == "win32"* ]]; then
    pyinstaller --distpath=build\dist --workpath=build\work --name=PIC app\main.py
else
    echo "Unknown OS: $OSTYPE"
    exit 1
fi