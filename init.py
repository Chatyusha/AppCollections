import os
import json

with open("config.json") as config_file:
    config = json.loads(config_file.read())
    for arch in config["archs"]:
        os.makedirs(arch)