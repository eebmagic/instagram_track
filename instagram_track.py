import requests
import time
import json

def parse_line(l):
    start = l.index('content="')+len('content="')
    end = l.index(' - ')
    l = l[start:end]

    out = {}
    for x in l.split(', '):
        x = x.split(' ')
        out[x[1]] = x[0]

    return out


# Constants
recordFilePATH = "/home/ethanbolton/pythonTools/instagram_check/pastData.json"
urlFile = "/home/ethanbolton/pythonTools/instagram_check/URL.txt"
key = '<meta property="og:description" content="'


# Make current time string
current_time = time.strftime('%Y/%m/%d - %X')
print(current_time)

# Load url
with open(urlFile) as file:
    url = file.read().strip()

r = requests.get(url)
r_html = r.text
lines = r_html.split('\n')

# Find and parse data
for line in lines:
    if key in line:
        print(line)
        values = parse_line(line)
        print(current_time, values)

# Open old data
with open(recordFilePATH, "r") as file:
	data = json.load(file)

data[current_time] = values
print(data)

# Save new data
with open(recordFilePATH, "w") as write_file:
	json.dump(data, write_file)
