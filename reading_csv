import requests
from contextlib import closing
import csv
import json
import pprint

"""
Following approach is chosen instead of panda library for 
maximizing the efficiency.

csv rows are read as ordered dictionary object and then converted
into json file format.

Finally, json string is printed to the console

"""

url = "https://www.football-data.co.uk/mmz4281/1920/E2.csv"

with closing(requests.get(url, stream=True)) as r:
    f = (line.decode('utf-8') for line in r.iter_lines())
    reader = csv.DictReader(f, delimiter=',', quotechar='"')       
    for i in reader:
        print(json.dumps(i, indent = 4))
