#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then save them to a file
"""

import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'

# check if file exists, if not create an empty list
if os.path.isfile(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# add arguments to list
for arg in sys.argv[1:]:
    my_list.append(arg)

# save list to file
save_to_json_file(my_list, filename)
