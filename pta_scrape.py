import requests
import json


url =""

r = requests.get(url, verify=False)

data = json.loads(r.content)

data = data[data.keys()[0]]



# Extract user_likes_count and dump to csv

fout = open('/Users///../brand_pta.csv', 'w')

for datapoint in data.get('storytellers_count'):

    date, count = datapoint

    fout.write('{},{}\n'.format(date, count))

fout.close()
