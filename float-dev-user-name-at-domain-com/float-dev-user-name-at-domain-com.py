
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id





c = 2.4

import json
filename = "/tmp/c_" + id + ".json"
file_c = open(filename, "w")
file_c.write(json.dumps(c))
file_c.close()
