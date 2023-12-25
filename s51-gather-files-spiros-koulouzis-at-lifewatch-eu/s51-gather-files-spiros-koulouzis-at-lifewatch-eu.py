import os
import pathlib
import shutil

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--local_path_targets', action='store', type=str, required='True', dest='local_path_targets')


args = arg_parser.parse_args()
print(args)

id = args.id

local_path_targets = args.local_path_targets


conf_local_path_targets = os.path.join( pathlib.Path('/tmp/data').as_posix(), 'targets')

conf_local_path_targets = os.path.join( pathlib.Path('/tmp/data').as_posix(), 'targets')



local_path_targets

targets_ply = '/tmp/data/targets/'
os.makedirs(targets_ply, exist_ok=True)

for root, dirs, files in os.walk(conf_local_path_targets):
    for dir_name in dirs:
        # Check for folders named 'perc_95_normalized_height'
        if dir_name == 'perc_95_normalized_height':
            ply_files = [
                file_name for file_name in os.listdir(os.path.join(root, dir_name))
                if file_name.endswith('.ply')
            ]

            # Move or copy the .ply files to the destination directory
            for ply_file in ply_files:
                file_path = os.path.join(root, dir_name, ply_file)
                shutil.copy(file_path, os.path.join(targets_ply, ply_file))

import json
filename = "/tmp/targets_ply_" + id + ".json"
file_targets_ply = open(filename, "w")
file_targets_ply.write(json.dumps(targets_ply))
file_targets_ply.close()
