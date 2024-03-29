from laserfarm import Retiler
import pathlib

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--split_laz_files', action='store', type=str, required=True, dest='split_laz_files')

arg_parser.add_argument('--param_hostname', action='store', type=str, required=True, dest='param_hostname')
arg_parser.add_argument('--param_login', action='store', type=str, required=True, dest='param_login')
arg_parser.add_argument('--param_max_x', action='store', type=str, required=True, dest='param_max_x')
arg_parser.add_argument('--param_max_y', action='store', type=str, required=True, dest='param_max_y')
arg_parser.add_argument('--param_min_x', action='store', type=str, required=True, dest='param_min_x')
arg_parser.add_argument('--param_min_y', action='store', type=str, required=True, dest='param_min_y')
arg_parser.add_argument('--param_n_tiles_side', action='store', type=str, required=True, dest='param_n_tiles_side')
arg_parser.add_argument('--param_password', action='store', type=str, required=True, dest='param_password')
arg_parser.add_argument('--param_remote_path_root', action='store', type=str, required=True, dest='param_remote_path_root')
arg_parser.add_argument('--param_username', action='store', type=str, required=True, dest='param_username')

args = arg_parser.parse_args()
print(args)

id = args.id

import json
split_laz_files = json.loads(args.split_laz_files)

param_hostname = args.param_hostname
param_login = args.param_login
param_max_x = args.param_max_x
param_max_y = args.param_max_y
param_min_x = args.param_min_x
param_min_y = args.param_min_y
param_n_tiles_side = args.param_n_tiles_side
param_password = args.param_password
param_remote_path_root = args.param_remote_path_root
param_username = args.param_username

conf_remote_path_split = pathlib.Path(param_remote_path_root + '/split_'+param_username)
conf_local_tmp = pathlib.Path('/tmp')
conf_remote_path_retiled = pathlib.Path(param_remote_path_root + '/retiled_'+param_username)
conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}
conf_remote_path_norm = pathlib.Path(param_remote_path_root + '/norm_'+param_username)

conf_remote_path_split = pathlib.Path(param_remote_path_root + '/split_'+param_username)
conf_local_tmp = pathlib.Path('/tmp')
conf_remote_path_retiled = pathlib.Path(param_remote_path_root + '/retiled_'+param_username)
conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}
conf_remote_path_norm = pathlib.Path(param_remote_path_root + '/norm_'+param_username)


remote_path_split = conf_remote_path_split

grid_retile = {
    'min_x': float(param_min_x),
    'max_x': float(param_max_x),
    'min_y': float(param_min_y),
    'max_y': float(param_max_y),
    'n_tiles_side': int(param_n_tiles_side)
}


retiling_input = {
    'setup_local_fs': {'tmp_folder': conf_local_tmp.as_posix()},
    'pullremote': conf_remote_path_split.as_posix(),
    'set_grid': grid_retile,
    'split_and_redistribute': {},
    'validate': {},
    'pushremote': conf_remote_path_retiled.as_posix(),
    'cleanlocalfs': {}
}


for file in split_laz_files:
    print('Retiling: '+file)
    retiler = Retiler(file, label=file).config(retiling_input).setup_webdav_client(conf_wd_opts)
    retiler_output = retiler.run()
    
remote_path_norm = str(conf_remote_path_norm)

import json
filename = "/tmp/remote_path_norm_" + id + ".json"
file_remote_path_norm = open(filename, "w")
file_remote_path_norm.write(json.dumps(remote_path_norm))
file_remote_path_norm.close()
