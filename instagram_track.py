import requests
import time
import json
import os
from pathlib import Path

container_path = '/'.join(os.path.realpath(__file__).split('/')[:-1]) + '/'

record_path = container_path + "pastData.json"
source_url_path = container_path + "URL.txt"

# Check for URL.txt file
if Path.is_file(Path(source_url_path)):
	with open(source_url_path) as file:
		url = file.read()
		print(url)
else:
	quit("# ERROR # - URL.txt file for source of instagram page not found.")

# Check for pastData.json file
if Path.is_file(Path(record_path)):
	print("pastData.json file was found!")
	pass
else:
	print("pastData.json file was NOT found")
	Path.touch(Path(record_path))
	with open(record_path, 'w') as file:
		file.write("{}")


current_time = time.strftime('%x - %X')
print(current_time)

r = requests.get(url)
r_html = r.text

labels = r_html[r_html.index('<meta content="') + len('<meta content="'):]
labels = labels[:labels.index(' - ')]
labels = labels.split(', ')

newData = {}
for label in labels:
	sections = label.split(' ')
	newData[sections[1]] = sections[0]

print(labels)
print(newData)

with open(record_path, "r") as file:
	oldData = json.load(file)

oldData[current_time] = newData

with open(record_path, "w") as write_file:
	json.dump(oldData, write_file)
