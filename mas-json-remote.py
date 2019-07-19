#json example
import json,requests,sys

#credd1 = input("Username:")
#credd = input("password:")
#url = input("IP or FQDN  of IBM Cloud Object Manager: ")
#cred = str(sec.b64decode('<base64code>'),"utf-8")
r = requests.get('https://%s/manager/api/json/1.0/driveReport.adm' % (url), verify=False, auth=(credd1, credd))

if r.status_code == 200:
    print(r.status_code)
else:
    print("Request failed, Please check the error code")
    print(r.status_code)
    sys.exit()
get = json.loads(r.content.decode('utf-8'))

print("Listing devices per site")
print("Site Name:  " + get["responseData"]["devices"][0]["site"]["name"])
for mas in get["responseData"]["devices"]:
    if "rio" in mas["alias"]:
        if "ONLINE" in mas["drives"][0]["status"]:
            drivecount = 0
            try:
                while drivecount < 75:
                    mike = mas["drives"][drivecount]["status"]
                    jackson = mas["id"]
                    print(mas["alias"] + "Device ID: %s " % str(jackson)  + " || Drive %s Status: " % str(drivecount)  + "||")

                    print(mike) 
                    drivecount += 1
            except IndexError:
                print("Reached max drive for device")
