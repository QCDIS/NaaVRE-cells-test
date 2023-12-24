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

conf_remote_path_geotiffs = pathlib.Path('/webdav/vl-laserfarm/' +  'spiros.koulouzis@lifewatch.eu' + '/geotiffs')
conf_num_files = 1
conf_mode = 'webdav'

conf_remote_path_geotiffs = pathlib.Path('/webdav/vl-laserfarm/' +  'spiros.koulouzis@lifewatch.eu' + '/geotiffs')
conf_num_files = 1
conf_mode = 'webdav'
hostname = param_hostname
username = param_username
password = param_password
remote = str(conf_remote_path_geotiffs)
num = conf_num_files
mode = conf_mode
output = '/tmp/data'

import json
filename = "/tmp/hostname_" + id + ".json"
file_hostname = open(filename, "w")
file_hostname.write(json.dumps(hostname))
file_hostname.close()
filename = "/tmp/username_" + id + ".json"
file_username = open(filename, "w")
file_username.write(json.dumps(username))
file_username.close()
filename = "/tmp/password_" + id + ".json"
file_password = open(filename, "w")
file_password.write(json.dumps(password))
file_password.close()
filename = "/tmp/remote_" + id + ".json"
file_remote = open(filename, "w")
file_remote.write(json.dumps(remote))
file_remote.close()
filename = "/tmp/num_" + id + ".json"
file_num = open(filename, "w")
file_num.write(json.dumps(num))
file_num.close()
filename = "/tmp/mode_" + id + ".json"
file_mode = open(filename, "w")
file_mode.write(json.dumps(mode))
file_mode.close()
filename = "/tmp/output_" + id + ".json"
file_output = open(filename, "w")
file_output.write(json.dumps(output))
file_output.close()
