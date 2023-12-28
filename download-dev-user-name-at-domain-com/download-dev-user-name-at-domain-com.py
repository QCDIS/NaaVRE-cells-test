from webdav3.client import Client
import os
import pathlib

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_hostname', action='store', type=str, required=True, dest='param_hostname')
arg_parser.add_argument('--param_password', action='store', type=str, required=True, dest='param_password')
arg_parser.add_argument('--param_username', action='store', type=str, required=True, dest='param_username')

args = arg_parser.parse_args()
print(args)

id = args.id


param_hostname = args.param_hostname
param_password = args.param_password
param_username = args.param_username

conf_local_path_geotiff = os.path.join( pathlib.Path('/tmp/data').as_posix(), 'geotiff')
conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_username, 'webdav_password': param_password}
conf_remote_path_geotiffs = pathlib.Path('/webdav/vl-laserfarm/' +  '' + '/geotiffs')

conf_local_path_geotiff = os.path.join( pathlib.Path('/tmp/data').as_posix(), 'geotiff')
conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_username, 'webdav_password': param_password}
conf_remote_path_geotiffs = pathlib.Path('/webdav/vl-laserfarm/' +  '' + '/geotiffs')


print(conf_local_path_geotiff)
if not os.path.exists(conf_local_path_geotiff):  # Check if folder doesn't exist
    os.makedirs(conf_local_path_geotiff)  # Create the folder

client = Client(conf_wd_opts)
client.download_sync(remote_path=os.path.join(conf_remote_path_geotiffs,'geotiff_TILE_000_BAND_perc_95_normalized_height.tif'), local_path=os.path.join(conf_local_path_geotiff,'geotiff_TILE_000_BAND_perc_95_normalized_height.tif'))

download_done = 'True'

import json
filename = "/tmp/download_done_" + id + ".json"
file_download_done = open(filename, "w")
file_download_done.write(json.dumps(download_done))
file_download_done.close()
