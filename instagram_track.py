import requests
import time
import json

recordFilePATH = "/home/ethanbolton/pythonTools/instagram_track/pastData.json"

current_time = time.strftime('%x - %X')
print(current_time)

url = "https://www.instagram.com/ee.bolton/"
r = requests.get(url)
r_html = r.text

labels = r_html[r_html.index('<meta content="')+len('<meta content="'):]
labels = labels[:labels.index(' - ')]
labels = labels.split(', ')

newData = {}
for label in labels:
	sections = label.split(' ')
	newData[sections[1]] = sections[0]

print(labels)
print(newData)

with open(recordFilePATH, "r") as file:
	oldData = json.load(file)

oldData[current_time] = newData

with open(recordFilePATH, "w") as write_file:
	json.dump(oldData, write_file)
