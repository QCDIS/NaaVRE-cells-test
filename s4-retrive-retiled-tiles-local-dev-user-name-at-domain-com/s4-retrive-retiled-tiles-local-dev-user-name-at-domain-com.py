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

path_retiled = local_path_retiled

import json
filename = "/tmp/tiles_" + id + ".json"
file_tiles = open(filename, "w")
file_tiles.write(json.dumps(tiles))
file_tiles.close()
filename = "/tmp/path_retiled_" + id + ".json"
file_path_retiled = open(filename, "w")
file_path_retiled.write(json.dumps(path_retiled))
file_path_retiled.close()
