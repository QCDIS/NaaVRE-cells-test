
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--values', action='store', type=str, required=True, dest='values')


args = arg_parser.parse_args()
print(args)

id = args.id

import json
values = json.loads(args.values)



for value in values:
    print(value)

