from webdav3.client import Client
import laspy
import numpy as np
import os
import pathlib

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--laz_files', action='store', type=str, required=True, dest='laz_files')

arg_parser.add_argument('--param_hostname', action='store', type=str, required='True', dest='param_hostname')
arg_parser.add_argument('--param_login', action='store', type=str, required='True', dest='param_login')
arg_parser.add_argument('--param_max_filesize', action='store', type=str, required='True', dest='param_max_filesize')
arg_parser.add_argument('--param_password', action='store', type=str, required='True', dest='param_password')
arg_parser.add_argument('--param_remote_path_root', action='store', type=str, required='True', dest='param_remote_path_root')

args = arg_parser.parse_args()
print(args)

id = args.id

import json
laz_files = json.loads(args.laz_files)

param_hostname = args.param_hostname
param_login = args.param_login
param_max_filesize = args.param_max_filesize
param_password = args.param_password
param_remote_path_root = args.param_remote_path_root

conf_laz_compression_factor = '7'
conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}
conf_remote_path_split = pathlib.Path('/webdav/vl-laserfarm/' +  'spiros.koulouzis@lifewatch.eu' + '/split')

conf_laz_compression_factor = '7'
conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}
conf_remote_path_split = pathlib.Path('/webdav/vl-laserfarm/' +  'spiros.koulouzis@lifewatch.eu' + '/split')


def save_chunk_to_laz_file(in_filename, 
                           out_filename, 
                           offset, 
                           n_points):
    """Read points from a LAS/LAZ file and write them to a new file."""
    points = np.array([])
    
    with laspy.open(in_filename) as in_file:
        with laspy.open(out_filename, 
                        mode="w", 
                        header=in_file.header) as out_file:
            in_file.seek(offset)
            points = in_file.read_points(n_points)
            out_file.write_points(points)
    return out_filename

def split_strategy(filename, max_filesize):
    """Set up splitting strategy for a LAS/LAZ file."""
    with laspy.open(filename) as f:
        bytes_per_point = (
            f.header.point_format.num_standard_bytes +
            f.header.point_format.num_extra_bytes
        )
        n_points = f.header.point_count
    n_points_target = int(
        max_filesize * int(conf_laz_compression_factor) / bytes_per_point
    )
    stem, ext = os.path.splitext(filename)
    return [
        (filename, f"{stem}-{n}{ext}", offset, n_points_target)
        for n, offset in enumerate(range(0, n_points, n_points_target))
    ]


client = Client(conf_wd_opts)
client.mkdir(conf_remote_path_split.as_posix())

remote_path_split = str(conf_remote_path_split)


for file in laz_files:
    print('Splitting: '+file )
    client.download_sync(remote_path=os.path.join(param_remote_path_root,file), local_path=file)
    inps = split_strategy(file, int(param_max_filesize)*1048576)
    
    
    for inp in inps:
        out_filename = save_chunk_to_laz_file(*inp)
        print('out_filename: '+out_filename)
        client.upload_sync(remote_path=os.path.join(conf_remote_path_split,out_filename), local_path=out_filename)
        # split_laz_files.append(out_filename)
    

import json
filename = "/tmp/remote_path_split_" + id + ".json"
file_remote_path_split = open(filename, "w")
file_remote_path_split.write(json.dumps(remote_path_split))
file_remote_path_split.close()
