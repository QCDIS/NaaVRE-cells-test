
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--numbers', action='store', type=str, required='True', dest='numbers')


args = arg_parser.parse_args()
print(args)

id = args.id

import json
numbers = json.loads(args.numbers.replace('\'','').replace('[','["').replace(']','"]'))



average <- mean(numbers)

import json
filename = "/tmp/average_" + id + ".json"
file_average = open(filename, "w")
file_average.write(json.dumps(average))
file_average.close()
