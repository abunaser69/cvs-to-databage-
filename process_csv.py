import requests
from contextlib import closing
import csv


"""
Here specific columns are selected from the csv file and write to a
temporary file for further processing
"""


url = "https://www.football-data.co.uk/mmz4281/1920/E2.csv"

colnames = ['Div', 'Date', 'Time', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']

with closing(requests.get(url, stream=True)) as r, open('out.csv','w') as out:
    f = (line.decode('utf-8') for line in r.iter_lines()) 
    dic_read = csv.DictReader(f)
    dic_write = csv.DictWriter(out, colnames, extrasaction='ignore')
    dic_write.writeheader()
    for row in dic_read:
        dic_write.writerow(row)
        
