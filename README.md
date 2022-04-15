# AutoJSON by YouTubeATP
## Introduction
This is a small Python script that automatically generates the `sounds.json` file in a Minecraft Java Edition resource pack, and also the `sounds/sound_definitions.json` file in a Minecraft Bedrock resource pack. It comes with an auto convert feature, so even if you put .mp3 or .wav files they will still be converted to .ogg and work.<br>
It can also generate `blocks.json` and `texture/terrain_textures.json` for custom blocks, for any png file inside `textures/blocks` starting with `cust_`.
## How to use
This script names sound event names based on the file's location in the `assets\minecraft\sounds` folder.<br/>For example, if a file called `hi.ogg` is stored in the `assets\minecraft\sounds\hello\hiya` folder, the following will be generated in `sounds.json`:

    "hello.hiya.hi": {
      "sounds": [
        {
          "name": "hello/hiya/hi"
        }
      ]
    }

<br>Blocks are also named like this based on their location.
### Dependencies
Dependencies are defined in the `requirements.txt` file.<br/>In a terminal, change to the `pack\python` directory and run `pip install -r requirements.txt`.
### Running
Simply run `autoJSON.py`, and the script will do all of the work.