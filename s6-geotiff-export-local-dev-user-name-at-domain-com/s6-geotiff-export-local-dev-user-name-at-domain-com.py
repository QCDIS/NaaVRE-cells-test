from laserfarm import GeotiffWriter
import os
import pathlib

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--local_path_targets', action='store', type=str, required=True, dest='local_path_targets')

arg_parser.add_argument('--param_hostname', action='store', type=str, required=True, dest='param_hostname')
arg_parser.add_argument('--param_password', action='store', type=str, required=True, dest='param_password')
arg_parser.add_argument('--param_username', action='store', type=str, required=True, dest='param_username')

args = arg_parser.parse_args()
print(args)

id = args.id

local_path_targets = args.local_path_targets.replace('"','')

param_hostname = args.param_hostname
param_password = args.param_password
param_username = args.param_username

conf_local_tmp = pathlib.Path('/tmp/data')
conf_remote_path_geotiffs = pathlib.Path('/webdav/vl-laserfarm/' +  'spiros.koulouzis@lifewatch.eu' + '/geotiffs')
conf_feature_name = 'perc_95_normalized_height'
conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_username, 'webdav_password': param_password}

conf_local_tmp = pathlib.Path('/tmp/data')
conf_remote_path_geotiffs = pathlib.Path('/webdav/vl-laserfarm/' +  'spiros.koulouzis@lifewatch.eu' + '/geotiffs')
conf_feature_name = 'perc_95_normalized_height'
conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_username, 'webdav_password': param_password}


local_path_geotiff = os.path.join(conf_local_tmp.as_posix(), 'geotiff')

geotiff_export_input = {
    'setup_local_fs': {
        'input_folder': local_path_targets,
         'output_folder': local_path_geotiff
        },
    # 'pullremote': conf_remote_path_targets.as_posix(),
    'parse_point_cloud': {},
    'data_split': {'xSub': 1, 'ySub': 1},
    'create_subregion_geotiffs': {'output_handle': 'geotiff'},
    'pushremote': conf_remote_path_geotiffs.as_posix(),
    'cleanlocalfs': {}   
}

writer = GeotiffWriter(input_dir=conf_feature_name, bands=conf_feature_name, label=conf_feature_name).config(geotiff_export_input).setup_webdav_client(conf_wd_opts)
writer.run()

remote_path_geotiffs = str(conf_remote_path_geotiffs)

import json
filename = "/tmp/remote_path_geotiffs_" + id + ".json"
file_remote_path_geotiffs = open(filename, "w")
file_remote_path_geotiffs.write(json.dumps(remote_path_geotiffs))
file_remote_path_geotiffs.close()
