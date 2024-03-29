
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--laz_files', action='store', type=str, required=True, dest='laz_files')


args = arg_parser.parse_args()
print(args)

id = args.id

import json
laz_files = json.loads(args.laz_files)


conf_data = '/tmp/data/'

conf_data = '/tmp/data/'

for file in laz_files:
    print('Splitting: '+file )
    with open(conf_data+file, 'r') as file:
        content = file.read()
    print(f"Contents of '{file}':")
    print(content)
    print('\n')  # Adding a new line for separation

