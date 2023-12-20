
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--a', action='store', type=int, required=True, dest='a')

arg_parser.add_argument('--param_a', action='store', type=int, required=True, dest='param_a')

args = arg_parser.parse_args()
print(args)

id = args.id

a = args.a

param_a = args.param_a

conf_a = 1

conf_a = 1
print(a, conf_a, param_a)

