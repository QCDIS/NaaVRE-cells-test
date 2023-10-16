
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id





msg = "Hello world!"

import json
filename = "/tmp/msg_" + id + ".json"
file_msg = open(filename, "w")
file_msg.write(json.dumps(msg))
file_msg.close()
