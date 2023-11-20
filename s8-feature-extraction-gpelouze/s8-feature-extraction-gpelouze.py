from laserfarm import DataProcessing
import pathlib

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--tiles', action='store', type=str, required=True, dest='tiles')

arg_parser.add_argument('--param_apply_filter_value', action='store', type=str, required='True', dest='param_apply_filter_value')
arg_parser.add_argument('--param_attribute', action='store', type=str, required='True', dest='param_attribute')
arg_parser.add_argument('--param_filter_type', action='store', type=str, required='True', dest='param_filter_type')
arg_parser.add_argument('--param_hostname', action='store', type=str, required='True', dest='param_hostname')
arg_parser.add_argument('--param_login', action='store', type=str, required='True', dest='param_login')
arg_parser.add_argument('--param_max_x', action='store', type=str, required='True', dest='param_max_x')
arg_parser.add_argument('--param_max_y', action='store', type=str, required='True', dest='param_max_y')
arg_parser.add_argument('--param_min_x', action='store', type=str, required='True', dest='param_min_x')
arg_parser.add_argument('--param_min_y', action='store', type=str, required='True', dest='param_min_y')
arg_parser.add_argument('--param_n_tiles_side', action='store', type=str, required='True', dest='param_n_tiles_side')
arg_parser.add_argument('--param_password', action='store', type=str, required='True', dest='param_password')
arg_parser.add_argument('--param_remote_path_root', action='store', type=str, required='True', dest='param_remote_path_root')
arg_parser.add_argument('--param_tile_mesh_size', action='store', type=str, required='True', dest='param_tile_mesh_size')
arg_parser.add_argument('--param_username', action='store', type=str, required='True', dest='param_username')
arg_parser.add_argument('--param_validate_precision', action='store', type=str, required='True', dest='param_validate_precision')

args = arg_parser.parse_args()
print(args)

id = args.id

import json
tiles = json.loads(args.tiles)

param_apply_filter_value = args.param_apply_filter_value
param_attribute = args.param_attribute
param_filter_type = args.param_filter_type
param_hostname = args.param_hostname
param_login = args.param_login
param_max_x = args.param_max_x
param_max_y = args.param_max_y
param_min_x = args.param_min_x
param_min_y = args.param_min_y
param_n_tiles_side = args.param_n_tiles_side
param_password = args.param_password
param_remote_path_root = args.param_remote_path_root
param_tile_mesh_size = args.param_tile_mesh_size
param_username = args.param_username
param_validate_precision = args.param_validate_precision

conf_remote_path_targets = pathlib.Path(param_remote_path_root + '/targets_'+param_username)
conf_local_tmp = pathlib.Path('/tmp')
conf_remote_path_norm = pathlib.Path(param_remote_path_root + '/norm_'+param_username)
conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}

conf_remote_path_targets = pathlib.Path(param_remote_path_root + '/targets_'+param_username)
conf_local_tmp = pathlib.Path('/tmp')
conf_remote_path_norm = pathlib.Path(param_remote_path_root + '/norm_'+param_username)
conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}
print(tiles)

remote_path_targets = str(conf_remote_path_targets)

features = ["perc_95_normalized_height"]

tile_mesh_size = float(param_tile_mesh_size)

grid_feature = {
    'min_x': float(param_min_x),
    'max_x': float(param_max_x),
    'min_y': float(param_min_y),
    'max_y': float(param_max_y),
    'n_tiles_side': int(param_n_tiles_side)
}

feature_extraction_input = {
    'setup_local_fs': {
        'input_folder': (conf_local_tmp / 'tile_input').as_posix(),
        'output_folder': (conf_local_tmp / 'tile_output').as_posix(),
    },
    'pullremote': conf_remote_path_norm.as_posix(),
    'load': {'attributes': [param_attribute]},
    'normalize': 1,
    'apply_filter': {
        'filter_type': param_filter_type, 
        'attribute': param_attribute,
        'value': [int(param_apply_filter_value)]#ground surface (2), water (9), buildings (6), artificial objects (26), vegetation (?), and unclassified (1)
    },
    'generate_targets': {
        'tile_mesh_size' : tile_mesh_size,
        'validate' : True,
        'validate_precision': float(param_validate_precision),
        **grid_feature
    },
    'extract_features': {
        'feature_names': features,
        'volume_type': 'cell',
        'volume_size': tile_mesh_size
    },
    'export_targets': {
        'attributes': features,
        'multi_band_files': False
    },
    'pushremote': conf_remote_path_targets.as_posix(),
}

for t in tiles:    
    idx = (t.split('.')[0].split('_')[1:])
    processing = DataProcessing(t, tile_index=idx,label=t).config(feature_extraction_input).setup_webdav_client(conf_wd_opts)
    processing.run()

print(remote_path_targets)

import json
filename = "/tmp/remote_path_targets_" + id + ".json"
file_remote_path_targets = open(filename, "w")
file_remote_path_targets.write(json.dumps(remote_path_targets))
file_remote_path_targets.close()
