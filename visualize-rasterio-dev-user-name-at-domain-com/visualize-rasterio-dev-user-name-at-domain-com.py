import os
import pathlib
from matplotlib import pyplot
import rasterio
from rasterio.plot import show
from rasterio.plot import show_hist

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--download_done', action='store', type=str, required=True, dest='download_done')


args = arg_parser.parse_args()
print(args)

id = args.id
parameters = {}

download_done = args.download_done.replace('"','')
parameters['download_done'] = download_done


conf_local_path_geotiff = os.path.join( pathlib.Path('/tmp/data').as_posix(), 'geotiff')
parameters['conf_local_path_geotiff'] = conf_local_path_geotiff



pm.execute_notebook(
    'visualize-rasterio-dev-user-name-at-domain-com.ipynb',
    'visualize-rasterio-dev-user-name-at-domain-com-output.ipynb',
    prepare_only=True,
    parameters=dict(msg=0.6)
)


