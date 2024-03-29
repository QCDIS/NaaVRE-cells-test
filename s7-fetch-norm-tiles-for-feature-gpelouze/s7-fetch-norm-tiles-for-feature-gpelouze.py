from laserfarm.remote_utils import get_wdclient
from laserfarm.remote_utils import list_remote
import pathlib

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--remote_path_norm', action='store', type=str, required='True', dest='remote_path_norm')

arg_parser.add_argument('--param_hostname', action='store', type=str, required='True', dest='param_hostname')
arg_parser.add_argument('--param_login', action='store', type=str, required='True', dest='param_login')
arg_parser.add_argument('--param_password', action='store', type=str, required='True', dest='param_password')
arg_parser.add_argument('--param_remote_path_root', action='store', type=str, required='True', dest='param_remote_path_root')
arg_parser.add_argument('--param_username', action='store', type=str, required='True', dest='param_username')

args = arg_parser.parse_args()
print(args)

id = args.id

remote_path_norm = args.remote_path_norm

param_hostname = args.param_hostname
param_login = args.param_login
param_password = args.param_password
param_remote_path_root = args.param_remote_path_root
param_username = args.param_username

conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}
conf_remote_path_norm = pathlib.Path(param_remote_path_root + '/norm_'+param_username)

conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}
conf_remote_path_norm = pathlib.Path(param_remote_path_root + '/norm_'+param_username)
print(remote_path_norm)

tiles = [f for f in list_remote(get_wdclient(conf_wd_opts), pathlib.Path(conf_remote_path_norm).as_posix())
             if f.lower().endswith('.laz')]

print(tiles)

import json
filename = "/tmp/tiles_" + id + ".json"
file_tiles = open(filename, "w")
file_tiles.write(json.dumps(tiles))
file_tiles.close()
