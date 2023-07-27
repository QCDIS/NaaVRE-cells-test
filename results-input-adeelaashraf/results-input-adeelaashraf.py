
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




hostname = 'a'
username = 'a'
password = 'a'
remote_file_path = 'a'
num_files = 'a'
mode = 'a'

import json
filename = "/tmp/password_" + id + ".json"
file_password = open(filename, "w")
file_password.write(json.dumps(password))
file_password.close()
filename = "/tmp/username_" + id + ".json"
file_username = open(filename, "w")
file_username.write(json.dumps(username))
file_username.close()
filename = "/tmp/num_files_" + id + ".json"
file_num_files = open(filename, "w")
file_num_files.write(json.dumps(num_files))
file_num_files.close()
filename = "/tmp/mode_" + id + ".json"
file_mode = open(filename, "w")
file_mode.write(json.dumps(mode))
file_mode.close()
filename = "/tmp/hostname_" + id + ".json"
file_hostname = open(filename, "w")
file_hostname.write(json.dumps(hostname))
file_hostname.close()
filename = "/tmp/remote_file_path_" + id + ".json"
file_remote_file_path = open(filename, "w")
file_remote_file_path.write(json.dumps(remote_file_path))
file_remote_file_path.close()
