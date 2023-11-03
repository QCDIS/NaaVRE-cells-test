
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--a', action='store', type=int, required='True', dest='a')

arg_parser.add_argument('--b', action='store', type=str, required=True, dest='b')

arg_parser.add_argument('--c', action='store', type=str, required='True', dest='c')

arg_parser.add_argument('--d', action='store', type=float, required='True', dest='d')

arg_parser.add_argument('--e', action='store', type=int, required='True', dest='e')

arg_parser.add_argument('--f', action='store', type=int, required='True', dest='f')


args = arg_parser.parse_args()
print(args)

id = args.id

a = args.a
import json
b = json.loads(args.b)
c = args.c
d = args.d
e = args.e
f = args.f



print(a, c, d, e, f)
for v in b:
    print(v)

