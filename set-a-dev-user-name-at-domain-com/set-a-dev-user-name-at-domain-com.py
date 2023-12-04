
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




a = 1
b = [1, 2]
c = 'string'
d = 1.3

import json
filename = "/tmp/a_" + id + ".json"
file_a = open(filename, "w")
file_a.write(json.dumps(a))
file_a.close()
filename = "/tmp/b_" + id + ".json"
file_b = open(filename, "w")
file_b.write(json.dumps(b))
file_b.close()
filename = "/tmp/c_" + id + ".json"
file_c = open(filename, "w")
file_c.write(json.dumps(c))
file_c.close()
filename = "/tmp/d_" + id + ".json"
file_d = open(filename, "w")
file_d.write(json.dumps(d))
file_d.close()
