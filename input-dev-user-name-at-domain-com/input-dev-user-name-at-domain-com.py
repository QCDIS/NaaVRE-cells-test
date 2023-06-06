
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




a = 2 
numbers <- c(a, 4, 6, 8, 10)

import json
filename = "/tmp/numbers_" + id + ".json"
file_numbers = open(filename, "w")
file_numbers.write(json.dumps(numbers))
file_numbers.close()
