from laserfarm import GeotiffWriter
import pathlib

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--remote_path_targets', action='store', type=str, required='True', dest='remote_path_targets')

arg_parser.add_argument('--param_feature_name', action='store', type=str, required='True', dest='param_feature_name')
arg_parser.add_argument('--param_hostname', action='store', type=str, required='True', dest='param_hostname')
arg_parser.add_argument('--param_login', action='store', type=str, required='True', dest='param_login')
arg_parser.add_argument('--param_password', action='store', type=str, required='True', dest='param_password')
arg_parser.add_argument('--param_remote_path_root', action='store', type=str, required='True', dest='param_remote_path_root')
arg_parser.add_argument('--param_username', action='store', type=str, required='True', dest='param_username')

args = arg_parser.parse_args()
print(args)

id = args.id

remote_path_targets = args.remote_path_targets

param_feature_name = args.param_feature_name
param_hostname = args.param_hostname
param_login = args.param_login
param_password = args.param_password
param_remote_path_root = args.param_remote_path_root
param_username = args.param_username

conf_remote_path_geotiffs = pathlib.Path(param_remote_path_root + '/geotiffs_'+param_username)
conf_local_tmp = pathlib.Path('/tmp')
conf_remote_path_targets = pathlib.Path(param_remote_path_root + '/targets_'+param_username)
conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}

conf_remote_path_geotiffs = pathlib.Path(param_remote_path_root + '/geotiffs_'+param_username)
conf_local_tmp = pathlib.Path('/tmp')
conf_remote_path_targets = pathlib.Path(param_remote_path_root + '/targets_'+param_username)
conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}

print(remote_path_targets)

remote_path_geotiffs = conf_remote_path_geotiffs

geotiff_export_input = {
    'setup_local_fs': {'tmp_folder': conf_local_tmp.as_posix()},
    'pullremote': conf_remote_path_targets.as_posix(),
    'parse_point_cloud': {},
    'data_split': {'xSub': 1, 'ySub': 1},
    'create_subregion_geotiffs': {'output_handle': 'geotiff'},
    'pushremote': remote_path_geotiffs.as_posix(),
    'cleanlocalfs': {}   
}

writer = GeotiffWriter(input_dir=param_feature_name, bands=param_feature_name,label=param_feature_name).config(geotiff_export_input).setup_webdav_client(conf_wd_opts)
writer.run()

