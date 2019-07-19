#json example

import json

r = open('mas1.json', 'r')

get = json.load(r)


#print(get["responseData"]["devices"])

print("Listing devices per site")
print("Site Name:  " + get["responseData"]["devices"][0]["site"]["name"])
for mas in get["responseData"]["devices"]:
    if "rio" in mas["alias"]:
        print(mas["alias"])
        print("Drive Status: " + mas["drives"][0]["status"])
