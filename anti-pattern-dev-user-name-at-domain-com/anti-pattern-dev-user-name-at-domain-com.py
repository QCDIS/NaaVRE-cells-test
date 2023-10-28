
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--count', action='store', type=int, required='True', dest='count')

arg_parser.add_argument('--msg', action='store', type=str, required='True', dest='msg')


args = arg_parser.parse_args()
print(args)

id = args.id

count = json.loads(args.count.replace("'", '' ))
msg = json.loads(args.msg.replace("'", '' ))



some_list = range(count, 100)
msg+= 'a'

