import glob
import os

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--local_path_retiled', action='store', type=str, required=True, dest='local_path_retiled')


args = arg_parser.parse_args()
print(args)

id = args.id

local_path_retiled = args.local_path_retiled.replace('"','')




tiles = []
tile_folders = glob.glob(os.path.join(local_path_retiled, 'tile_*_*'))

for folder in tile_folders:
    # Extract only the folder name without the 'local_path_retiled'
    folder_name = os.path.basename(folder)
    tiles.append(folder_name)  # Append only the folder name
print(tiles)

import json
filename = "/tmp/tiles_" + id + ".json"
file_tiles = open(filename, "w")
file_tiles.write(json.dumps(tiles))
file_tiles.close()
