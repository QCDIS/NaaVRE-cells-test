from laserfarm import Retiler
import os
import pathlib

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--local_path_split', action='store', type=str, required=True, dest='local_path_split')

arg_parser.add_argument('--split_laz_files', action='store', type=str, required=True, dest='split_laz_files')


args = arg_parser.parse_args()
print(args)

id = args.id

local_path_split = args.local_path_split.replace('"','')
import json
split_laz_files = json.loads(args.split_laz_files)


conf_local_tmp = pathlib.Path('/tmp/data')
conf_min_x = '-113107.81'
conf_max_x = '398892.19'
conf_min_y = '214783.87'
conf_max_y = '726783.87'
conf_n_tiles_side = '512'

conf_local_tmp = pathlib.Path('/tmp/data')
conf_min_x = '-113107.81'
conf_max_x = '398892.19'
conf_min_y = '214783.87'
conf_max_y = '726783.87'
conf_n_tiles_side = '512'
split_laz_files

local_path_retiled = os.path.join(conf_local_tmp.as_posix(), 'retiled')

grid_retile = {
    'min_x': float(conf_min_x),
    'max_x': float(conf_max_x),
    'min_y': float(conf_min_y),
    'max_y': float(conf_max_y),
    'n_tiles_side': int(conf_n_tiles_side)
}

retiling_input = {
    # 'setup_local_fs': {'tmp_folder': conf_local_tmp.as_posix()},
    'setup_local_fs': {
        'input_folder': local_path_split,
        'output_folder': local_path_retiled
    },
    # 'pullremote': conf_remote_path_split.as_posix(),
    'set_grid': grid_retile,
    'split_and_redistribute': {},
    'validate': {},
    # 'pushremote': conf_remote_path_retiled.as_posix(),
    # 'cleanlocalfs': {}
}

for file in split_laz_files:
    clean_file = file.replace('"','').replace('[','').replace(']','')
    print(clean_file)
    # retiler = Retiler(clean_file,label=clean_file).config(retiling_input).setup_webdav_client(conf_wd_opts)
    retiler = Retiler(clean_file,label=clean_file).config(retiling_input)
    retiler_output = retiler.run()

import json
filename = "/tmp/local_path_retiled_" + id + ".json"
file_local_path_retiled = open(filename, "w")
file_local_path_retiled.write(json.dumps(local_path_retiled))
file_local_path_retiled.close()
