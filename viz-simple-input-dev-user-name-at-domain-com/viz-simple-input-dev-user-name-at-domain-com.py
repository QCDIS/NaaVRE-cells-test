
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_geotiff_path', action='store', type=str, required='True', dest='param_geotiff_path')
arg_parser.add_argument('--param_hostname', action='store', type=str, required='True', dest='param_hostname')
arg_parser.add_argument('--param_login', action='store', type=str, required='True', dest='param_login')
arg_parser.add_argument('--param_password', action='store', type=str, required='True', dest='param_password')

args = arg_parser.parse_args()
print(args)

id = args.id


param_geotiff_path = args.param_geotiff_path
param_hostname = args.param_hostname
param_login = args.param_login
param_password = args.param_password



viz_input = [param_hostname, param_login, param_password, param_geotiff_path]

import json
filename = "/tmp/viz_input_" + id + ".json"
file_viz_input = open(filename, "w")
file_viz_input.write(json.dumps(viz_input))
file_viz_input.close()
