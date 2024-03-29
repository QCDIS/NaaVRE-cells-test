from minio import Minio
from laserfarm.remote_utils import get_wdclient
from laserfarm.remote_utils import list_remote
import pathlib

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_hostname', action='store', type=str, required=True, dest='param_hostname')
arg_parser.add_argument('--param_password', action='store', type=str, required=True, dest='param_password')
arg_parser.add_argument('--param_remote_server_type', action='store', type=str, required=True, dest='param_remote_server_type')
arg_parser.add_argument('--param_username', action='store', type=str, required=True, dest='param_username')

args = arg_parser.parse_args()
print(args)

id = args.id


param_hostname = args.param_hostname
param_password = args.param_password
param_remote_server_type = args.param_remote_server_type
param_username = args.param_username

conf_minio_server = hostname+':'+port

conf_bucket_name = path_parts[0]

conf_remote_path_root = '/'.join(path_parts[1:])

conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_username, 'webdav_password': param_password}


conf_minio_server = hostname+':'+port
conf_bucket_name = path_parts[0]
conf_remote_path_root = '/'.join(path_parts[1:])
conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_username, 'webdav_password': param_password}


laz_files = []
if param_remote_server_type == 'minio':
    minio_client = Minio(conf_minio_server, secure=True)
    objects = minio_client.list_objects(conf_bucket_name, prefix=conf_remote_path_root, recursive=True)
    for obj in objects:
        if obj.object_name.lower().endswith('.laz'):
            laz_files.append(obj.object_name.split('/')[-1])
elif param_remote_server_type == 'webdav':
    print(conf_remote_path_root)
    webdva_path = conf_remote_path_root
    laz_files = [f for f in list_remote(get_wdclient(conf_wd_opts), pathlib.Path(webdva_path).as_posix())
                 if f.lower().endswith('.laz')]
print(laz_files)

import json
filename = "/tmp/laz_files_" + id + ".json"
file_laz_files = open(filename, "w")
file_laz_files.write(json.dumps(laz_files))
file_laz_files.close()
