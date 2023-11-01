# Description: Make exe file for 
# make dir
mkdir -p build/dist
mkdir -p build/work

# build
pyinstaller --distpath=build/dist --workpath=build/work --name=PIC app/main.py