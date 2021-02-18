import os
from pydub import AudioSegment
import json

sounds = {}

def addEntry(path):
    mcPath = os.path.relpath(path, start="../assets/minecraft/sounds").replace("./", "", 1)[:-4] # Replace leading "./" and remove file extension
    mcPathTop = mcPath.replace("/", ".").replace("\\", ".")
    mcPathBottom = mcPath.replace("\\", "/")
    sounds[mcPathTop] = {"sounds": [{"name": mcPathBottom}]}
    print(f"Added entry for {os.path.relpath(path)}\nEvent name: {mcPathTop}\n\n")

for root, dirs, files in os.walk("../assets/minecraft/sounds", topdown=False):
    for name in files:
        if name.endswith(".mp3"):
            file = AudioSegment.from_file(os.path.join(root, name), format="mp3")
            file.export(os.path.join(root, name).replace(".mp3", ".ogg"), format="ogg")
            os.remove(os.path.join(root, name))
            print(f"Converted {os.path.join(root, name)}")
            addEntry(os.path.abspath(os.path.join(root, name)))
        elif name.endswith(".wav"):
            file = AudioSegment.from_file(os.path.join(root, name), format="wav")
            file.export(os.path.join(root, name).replace(".wav", ".ogg"), format="ogg")
            os.remove(os.path.join(root, name))
            print(f"Converted {os.path.join(root, name)}")
            addEntry(os.path.abspath(os.path.join(root, name)))
        elif name.endswith(".ogg"):
            addEntry(os.path.abspath(os.path.join(root, name)))
            
with open("../assets/minecraft/sounds.json", "w") as f:
    json.dump(sounds, f, indent=2)