import csv
import getopt
import json
import sys

json_file_path = None

try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:d:u:p:H:P:")
except getopt.GetoptError:
    print('main.py -i <import-file-path>')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print ('main.py -i <import-file-path>')
        sys.exit()
    elif opt in ("-i", "--import-file-path"):
        json_file_path = arg
        print("Using", json_file_path, "for import file path")

if json_file_path is None:
    print("ERROR: Please provide an import file path (-i, --import-file-path)")
    sys.exit()

json_file_reader = open(json_file_path, 'r')

json_file = json.loads(json_file_reader.read())

# print(json_file)