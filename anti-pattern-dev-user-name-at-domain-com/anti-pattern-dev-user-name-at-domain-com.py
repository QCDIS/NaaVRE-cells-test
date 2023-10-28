
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--b', action='store', type=int, required='True', dest='b')

arg_parser.add_argument('--count', action='store', type=int, required='True', dest='count')


args = arg_parser.parse_args()
print(args)

id = args.id

import json
b = json.loads(args.b)
count = json.loads(args.count)



some_list = range(count, b+1)

msg = '1'

import json
filename = "/tmp/msg_" + id + ".json"
file_msg = open(filename, "w")
file_msg.write(json.dumps(msg))
file_msg.close()
