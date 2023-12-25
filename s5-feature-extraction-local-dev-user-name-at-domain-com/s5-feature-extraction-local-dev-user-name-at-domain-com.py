from laserfarm import DataProcessing
import os
import pathlib

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--local_path_retiled', action='store', type=str, required=True, dest='local_path_retiled')

arg_parser.add_argument('--tiles', action='store', type=str, required=True, dest='tiles')


args = arg_parser.parse_args()
print(args)

id = args.id

local_path_retiled = args.local_path_retiled.replace('"','')
import json
tiles = json.loads(args.tiles)


conf_local_tmp = pathlib.Path('/tmp/data')
conf_feature_name = 'perc_95_normalized_height'
conf_tile_mesh_size = '10.'
conf_min_x = '-113107.81'
conf_max_x = '398892.19'
conf_min_y = '214783.87'
conf_max_y = '726783.87'
conf_n_tiles_side = '512'
conf_attribute = 'raw_classification'
conf_filter_type= 'select_equal'
conf_apply_filter_value = '1'
conf_validate_precision = '0.001'

conf_local_tmp = pathlib.Path('/tmp/data')
conf_feature_name = 'perc_95_normalized_height'
conf_tile_mesh_size = '10.'
conf_min_x = '-113107.81'
conf_max_x = '398892.19'
conf_min_y = '214783.87'
conf_max_y = '726783.87'
conf_n_tiles_side = '512'
conf_attribute = 'raw_classification'
conf_filter_type= 'select_equal'
conf_apply_filter_value = '1'
conf_validate_precision = '0.001'
    
local_path_targets = os.path.join(conf_local_tmp.as_posix(), 'targets')

for t in tiles:
    features = [conf_feature_name]

    tile_mesh_size = float(conf_tile_mesh_size)

    grid_feature = {
        'min_x': float(conf_min_x),
        'max_x': float(conf_max_x),
        'min_y': float(conf_min_y),
        'max_y': float(conf_max_y),
        'n_tiles_side': int(conf_n_tiles_side)
    }

    feature_extraction_input = {
        'setup_local_fs': {
        'input_folder': local_path_retiled,
        'output_folder': local_path_targets
        },
        # 'setup_local_fs': {'tmp_folder': conf_local_tmp.as_posix()},
        # 'pullremote': conf_remote_path_retiled.as_posix(),
        'load': {'attributes': [conf_attribute]},
        'normalize': 1,
        'apply_filter': {
            'filter_type': conf_filter_type, 
            'attribute': conf_attribute,
            'value': [int(conf_apply_filter_value)]#ground surface (2), water (9), buildings (6), artificial objects (26), vegetation (?), and unclassified (1)
        },
        'generate_targets': {
            'tile_mesh_size' : tile_mesh_size,
            'validate' : True,
            'validate_precision': float(conf_validate_precision),
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
        # 'pushremote': conf_remote_path_targets.as_posix(),
    #     'cleanlocalfs': {}
    }
    idx = (t.split('_')[1:])

    # processing = DataProcessing(t, tile_index=idx,label=t).config(feature_extraction_input).setup_webdav_client(conf_wd_opts)
    processing = DataProcessing(t, tile_index=idx,label=t).config(feature_extraction_input)
    processing.run()
    

import json
filename = "/tmp/local_path_targets_" + id + ".json"
file_local_path_targets = open(filename, "w")
file_local_path_targets.write(json.dumps(local_path_targets))
file_local_path_targets.close()
