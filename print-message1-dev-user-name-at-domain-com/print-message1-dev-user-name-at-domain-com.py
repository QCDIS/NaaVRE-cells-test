
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--msg', action='store', type=str, required='True', dest='msg')


args = arg_parser.parse_args()
print(args)

id = args.id

import json
msg = json.loads(args.msg.replace('\'', ''))



print(msg)

