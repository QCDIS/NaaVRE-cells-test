
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id



conf_filter_type= 'select_equal'

conf_filter_type= 'select_equal'

feature_extraction_input = {conf_filter_type}
    
    

import json
filename = "/tmp/feature_extraction_input_" + id + ".json"
file_feature_extraction_input = open(filename, "w")
file_feature_extraction_input.write(json.dumps(feature_extraction_input))
file_feature_extraction_input.close()
