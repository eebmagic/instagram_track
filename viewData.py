import json
import os

container_path = '/'.join(os.path.realpath(__file__).split('/')[:-1]) + '/'

record_path = container_path + "pastData.json"

with open(record_path, 'r') as file:
	oldData = json.load(file)

header = "Time                 |  Followers \tFollowing \tPosts"
print(header)
print("-" * (len(header)+ 10))
for time, data in oldData.items():
	print(f"{time}  |  {data['Followers']} \t\t{data['Following']} \t\t{data['Posts']}")