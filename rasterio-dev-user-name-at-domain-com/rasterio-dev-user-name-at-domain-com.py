import os
from matplotlib import pyplot
import rasterio
from rasterio.plot import show
from rasterio.plot import show_hist

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--download_done', action='store', type=str, required=True, dest='download_done')

arg_parser.add_argument('--local_path_geotiff', action='store', type=str, required=True, dest='local_path_geotiff')


args = arg_parser.parse_args()
print(args)

id = args.id

download_done = args.download_done.replace('"','')
local_path_geotiff = args.local_path_geotiff.replace('"','')




download_done

geo_tiff = os.path.join(local_path_geotiff, 'geotiff_TILE_000_BAND_perc_95_normalized_height.tif')
src = rasterio.open(geo_tiff)
show(src)
fig, ax = pyplot.subplots(1, figsize=(30, 30))
show((src, 1), interpolation='none', ax=ax)
show((src, 1), contour=True, ax=ax)
pyplot.show()
show_hist(src, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Histogram")
pyplot.show()
src.close()

