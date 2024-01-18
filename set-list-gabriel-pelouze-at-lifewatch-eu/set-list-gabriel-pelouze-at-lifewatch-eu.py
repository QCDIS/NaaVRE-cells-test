
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




values = [1, 2, 3, 4]

import json
filename = "/tmp/values_" + id + ".json"
file_values = open(filename, "w")
file_values.write(json.dumps(values))
file_values.close()
