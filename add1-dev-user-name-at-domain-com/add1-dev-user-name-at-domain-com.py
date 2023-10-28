
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--count', action='store', type=int, required='True', dest='count')


args = arg_parser.parse_args()
print(args)

id = args.id

import json
count = args.count




b = count + 1

import json
filename = "/tmp/b_" + id + ".json"
file_b = open(filename, "w")
file_b.write(json.dumps(b))
file_b.close()
