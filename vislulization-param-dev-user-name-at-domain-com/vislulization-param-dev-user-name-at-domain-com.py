import pathlib

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_hostname', action='store', type=str, required=True, dest='param_hostname')
arg_parser.add_argument('--param_login', action='store', type=str, required=True, dest='param_login')
arg_parser.add_argument('--param_password', action='store', type=str, required=True, dest='param_password')

args = arg_parser.parse_args()
print(args)

id = args.id


param_hostname = args.param_hostname
param_login = args.param_login
param_password = args.param_password

conf_remote_path_geotiffs = pathlib.Path('/webdav/vl-laserfarm/' +  'spiros.koulouzis@lifewatch.eu' + '/geotiffs')
conf_num_files = 1
conf_mode = 'webdav'

conf_remote_path_geotiffs = pathlib.Path('/webdav/vl-laserfarm/' +  'spiros.koulouzis@lifewatch.eu' + '/geotiffs')
conf_num_files = 1
conf_mode = 'webdav'
hostname = param_hostname
login = param_login
password = param_password
remote_path_geotiffs = str(conf_remote_path_geotiffs)
num_files = conf_num_files
mode = conf_mode

import json
filename = "/tmp/hostname_" + id + ".json"
file_hostname = open(filename, "w")
file_hostname.write(json.dumps(hostname))
file_hostname.close()
filename = "/tmp/login_" + id + ".json"
file_login = open(filename, "w")
file_login.write(json.dumps(login))
file_login.close()
filename = "/tmp/password_" + id + ".json"
file_password = open(filename, "w")
file_password.write(json.dumps(password))
file_password.close()
filename = "/tmp/remote_path_geotiffs_" + id + ".json"
file_remote_path_geotiffs = open(filename, "w")
file_remote_path_geotiffs.write(json.dumps(remote_path_geotiffs))
file_remote_path_geotiffs.close()
filename = "/tmp/num_files_" + id + ".json"
file_num_files = open(filename, "w")
file_num_files.write(json.dumps(num_files))
file_num_files.close()
filename = "/tmp/mode_" + id + ".json"
file_mode = open(filename, "w")
file_mode.write(json.dumps(mode))
file_mode.close()
