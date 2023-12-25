import glob
import os
import pathlib

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--local_path_split', action='store', type=str, required='True', dest='local_path_split')


args = arg_parser.parse_args()
print(args)

id = args.id

local_path_split = args.local_path_split


conf_local_path_split = os.path.join( pathlib.Path('/tmp/data').as_posix(), 'split')

conf_local_path_split = os.path.join( pathlib.Path('/tmp/data').as_posix(), 'split')
local_path_split
split_laz_folder = glob.glob(os.path.join(conf_local_path_split, '*.LAZ'))
split_laz_files = []
print("File names ending with .LAZ:")
for file_path in split_laz_folder:
    split_laz_files.append(os.path.basename(file_path))

print(split_laz_files)
    

import json
filename = "/tmp/split_laz_files_" + id + ".json"
file_split_laz_files = open(filename, "w")
file_split_laz_files.write(json.dumps(split_laz_files))
file_split_laz_files.close()
