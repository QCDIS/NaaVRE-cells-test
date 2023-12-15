import random
import string

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id





laz_files = []
num_files = 3 
conf_data = '/tmp/data/'
for i in range(num_files):
    file_name = ''.join(random.choices(string.ascii_lowercase, k=8)) + '.txt'  # Random file name
    laz_files.append(file_name)
    file_content = 'file_content'

    with open(conf_data+file_name, 'w') as file:
        file.write(file_content)
        print(f"File '{file_name}' created with random content.")
            

import json
filename = "/tmp/laz_files_" + id + ".json"
file_laz_files = open(filename, "w")
file_laz_files.write(json.dumps(laz_files))
file_laz_files.close()
filename = "/tmp/file_name_" + id + ".json"
file_file_name = open(filename, "w")
file_file_name.write(json.dumps(file_name))
file_file_name.close()
