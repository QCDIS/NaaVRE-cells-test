import os

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id





cmd = "vol2bird --version"

returned_value = os.system(cmd)  # returns the exit code in unix


import json
filename = "/tmp/returned_value_" + id + ".json"
file_returned_value = open(filename, "w")
file_returned_value.write(json.dumps(returned_value))
file_returned_value.close()
