import json

jsonPATH = "/home/ethanbolton/pythonTools/instagram_track/pastData.json"

with open(jsonPATH, 'r') as file:
    oldData = json.load(file)

header = "Time                 |  Followers \tFollowing \tPosts"
border = "-" * (len(header) + 10)

print(header)
print(border)

keys = oldData.keys()
keys = list(keys)
keys.sort()

for time in keys:
    data = oldData[time]
    print(f"{time}  |  {data['Followers']} \t\t{data['Following']} \t\t{data['Posts']}")

print(border)
print(header)

userResp = input("\n\tSend pastData.json to Drive? (Y/n): ").lower()
if userResp != 'n':
    import os
    print("Uploading...")
    os.system("rclone copy /home/ethanbolton/pythonTools/instagram_track/pastData.json Drive:/fromRclone/")
    print("Finished uploading to Drive:/fromRclone/")
