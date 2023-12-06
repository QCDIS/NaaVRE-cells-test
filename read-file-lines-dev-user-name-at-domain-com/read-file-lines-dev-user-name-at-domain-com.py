
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--file_path', action='store', type=str, required='True', dest='file_path')


args = arg_parser.parse_args()
print(args)

id = args.id

file_path = args.file_path




f = open(file_path, 'r')
lines = f.readlines()
f.close()

import json
filename = "/tmp/lines_" + id + ".json"
file_lines = open(filename, "w")
file_lines.write(json.dumps(lines))
file_lines.close()
