from laserfarm import Retiler
import pathlib

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--split_laz_files', action='store', type=str, required=True, dest='split_laz_files')

arg_parser.add_argument('--param_hostname', action='store', type=str, required='True', dest='param_hostname')
arg_parser.add_argument('--param_login', action='store', type=str, required='True', dest='param_login')
arg_parser.add_argument('--param_password', action='store', type=str, required='True', dest='param_password')
arg_parser.add_argument('--param_username', action='store', type=str, required='True', dest='param_username')

args = arg_parser.parse_args()
print(args)

id = args.id

import json
split_laz_files = json.loads(args.split_laz_files)

param_hostname = args.param_hostname
param_login = args.param_login
param_password = args.param_password
param_username = args.param_username

conf_remote_path_retiled = pathlib.Path( '/webdav/vl-laserfarm/ahn' + '/retiled_'+param_username)
conf_min_x = '-113107.81'
conf_max_x = '398892.19'
conf_min_y = '214783.87'
conf_max_y = '726783.87'
conf_n_tiles_side = '512'
conf_local_tmp = pathlib.Path('/tmp')
conf_remote_path_split = pathlib.Path( '/webdav/vl-laserfarm/ahn' + '/split_'+param_username)
conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}

conf_remote_path_retiled = pathlib.Path( '/webdav/vl-laserfarm/ahn' + '/retiled_'+param_username)
conf_min_x = '-113107.81'
conf_max_x = '398892.19'
conf_min_y = '214783.87'
conf_max_y = '726783.87'
conf_n_tiles_side = '512'
conf_local_tmp = pathlib.Path('/tmp')
conf_remote_path_split = pathlib.Path( '/webdav/vl-laserfarm/ahn' + '/split_'+param_username)
conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}
split_laz_files
remote_path_retiled = str(conf_remote_path_retiled)

grid_retile = {
    'min_x': float(conf_min_x),
    'max_x': float(conf_max_x),
    'min_y': float(conf_min_y),
    'max_y': float(conf_max_y),
    'n_tiles_side': int(conf_n_tiles_side)
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
    retiler = Retiler(file.replace('"',''),label=file).config(retiling_input).setup_webdav_client(conf_wd_opts)
    retiler_output = retiler.run()

import json
filename = "/tmp/remote_path_retiled_" + id + ".json"
file_remote_path_retiled = open(filename, "w")
file_remote_path_retiled.write(json.dumps(remote_path_retiled))
file_remote_path_retiled.close()
filename = "/tmp/retiler_output_" + id + ".json"
file_retiler_output = open(filename, "w")
file_retiler_output.write(json.dumps(retiler_output))
file_retiler_output.close()
