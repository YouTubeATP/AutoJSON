import os
from PIL import Image
from pydub import AudioSegment
import json

def je():
    sounds = {}

    def addEntry(path):
        mcPath = os.path.relpath(path, start=root_path + "/assets/minecraft/sounds").replace("./", "", 1)[:-4] # Replace leading "./" and remove file extension
        mcPathTop = mcPath.replace("/", ".").replace("\\", ".")
        mcPathBottom = mcPath.replace("\\", "/")
        sounds[mcPathTop] = {"sounds": [{"name": mcPathBottom}]}
        print(f"Added entry for {os.path.relpath(path)}\nEvent name: {mcPathTop}\n\n")

    for root, dirs, files in os.walk(root_path + "/assets/minecraft/sounds", topdown=False):
        for name in files:
            if not name.endswith(".ogg"):
                try:
                    file_type = name[name.rfind(".") + 1:]
                    file = AudioSegment.from_file(os.path.join(root, name), format="mp3")
                    file.export(os.path.join(root, name).replace(".mp3", ".ogg"), format="ogg")
                    os.remove(os.path.join(root, name))
                    print(f"Converted {os.path.join(root, name)}")
                except Exception:
                    print("An error occurred while converting " + os.path.join(root, name) + ". Most likely the file format is not supported.")
                    continue
            addEntry(os.path.abspath(os.path.join(root, name)))
                
    with open("../assets/minecraft/sounds.json", "w") as f:
        json.dump(sounds, f, indent=2)
        
def be():
    sounds = {"individual_event_sounds": {"events": {}}}
    defs = {}
    
    def addEntry(path):
        mcPathTop = os.path.relpath(path, start=root_path + "/sounds").replace("./", "", 1)[:-4].replace("/", ".").replace("\\", ".") # Replace leading "./" and remove file extension
        mcPathBottom = os.path.relpath(path, start=root_path + "/").replace("./", "", 1)[:-4].replace("\\", "/")
        defs[mcPathTop] = {"sounds": [mcPathBottom]}
        sounds["individual_event_sounds"]["events"][mcPathTop] = {"sound": mcPathTop, "volume": 1, "pitch": 1.0}
        print(f"Added entry for {os.path.relpath(path)}\nEvent name: {mcPathTop}\n\n")
    
    for root, dirs, files in os.walk(root_path + "/sounds", topdown=False):
        for name in files:
            if not name.endswith(".ogg"):
                try:
                    file_type = name[name.rfind(".") + 1:]
                    file = AudioSegment.from_file(os.path.join(root, name), format="mp3")
                    file.export(os.path.join(root, name).replace(".mp3", ".ogg"), format="ogg")
                    os.remove(os.path.join(root, name))
                    print(f"Converted {os.path.join(root, name)}")
                except Exception:
                    print("An error occurred while converting " + os.path.join(root, name) + ". Most likely the file format is not supported.")
                    continue
            addEntry(os.path.abspath(os.path.join(root, name)))
                
    with open(root_path + "/sounds.json", "w") as f:
        json.dump(sounds, f, indent=2)
        
    with open(root_path + "/sounds/sound_definitions.json", "w") as f:
        json.dump(defs, f, indent=2)
        
def block():
    blocks = {"format_version": "1.16.0"}
    terrain_texture = {"resource_pack_name": pack_name, "texture_name": "atlas.terrain", "padding": 0, "num_mip_levels": 0, "texture_data": {}}
    
    def addEntry(path):
        mcPathTop = namespace + os.path.relpath(path, start=root_path + "/textures/blocks").replace("./", "", 1)[:-4].replace("/", ".").replace("\\", ".") # Replace leading "./" and remove file extension
        mcPathBottom = os.path.relpath(path, start=root_path + "/textures/blocks").replace("./", "", 1)[:-4].replace("/", ".").replace("\\", ".") # Replace leading "./" and remove file extension
        mcPathTexturePath = os.path.relpath(path, start=root_path + "/").replace("./", "", 1)[:-4].replace("\\", "/")
        blocks[mcPathTop] = {"textures": mcPathBottom, "sound": "stone"}
        terrain_texture["texture_data"][mcPathBottom] = {"textures": mcPathTexturePath}
        print(f"Added entry for {os.path.relpath(path)}\nEvent name: {mcPathTop}\n\n")
    
    for root, dirs, files in os.walk(root_path + "/textures/blocks", topdown=False):
        for name in files:
            if not name.startswith("cust_"):
                continue
            if not name.endswith(".png"):
                try:
                    image = Image.open(os.path.join(root, name))
                    image.save(os.path.join(root, name)[:os.path.join(root, name).rfind(".")] + ".png")
                    os.remove(os.path.join(root, name))
                    print(f"Converted {os.path.join(root, name)}")
                except Exception:
                    print("An error occurred while converting " + os.path.join(root, name) + ". Most likely the file format is not supported.")
                    continue
            addEntry(os.path.abspath(os.path.join(root, name)))
            
    with open(root_path + "/blocks.json", "w") as f:
        json.dump(blocks, f, indent=2)
        
    with open(root_path + "/textures/terrain_texture.json", "w") as f:
        json.dump(terrain_texture, f, indent=2)
        
def main():
    while True:
        print("Welcome to AutoJSON!\n\nType \"je\" if your resource pack is for Java Edition.\nType \"be\" if your resource pack is for Bedrock Edition.\nType \"block\" if you want to generate custom blocks for Bedrock Edition.\n\nType \"exit\" to exit.\n")
        cmd = input("AutoJSON >> ")
        
        if cmd != "exit":
            global root_path
            root_path = input("Input the root path of this pack (the folder with manifest.json): ")
            if root_path.endswith("/"):
                root_path = root_path[:-1]
            
        if cmd == "je":
            je()
        elif cmd == "be":
            be()
        elif cmd == "block":
            global namespace
            namespace = input("Input the namespace of your pack: ")
            global pack_name
            pack_name = input("Input your pack name: ")
            block()
        elif cmd == "exit":
            print("See you next time!\n")
            exit()
        else:
            print("Invalid command!\n")

if __name__ == "__main__":            
    main()