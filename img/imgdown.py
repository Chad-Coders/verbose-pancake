import csv
import json
import shutil
import urllib.request

import requests

l = list(range(0))

with open('providers_se.csv') as file:
    reader = csv.reader(file, quoting=csv.QUOTE_ALL)
    for row in reader:
        l.append(row)

for x in range(len(l)):
    if(x%2 == 1):
        res = requests.get('https://www.justwatch.com/images' + l[x][0] + 's100', stream=True)
        if res.status_code == 200:
            with open(l[x-1][0] + '.png','wb') as f:
                shutil.copyfileobj(res.raw, f)
        else:
            print(res.status_code)

    


