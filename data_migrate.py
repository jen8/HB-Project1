import json

mynewhandle = open("SFPD_VerySimple.csv", "r")
count = 0
jsonlist = []
while True:                            # Keep reading forever
    theline = mynewhandle.readline()   # Try to read next line
    if len(theline) == 0:              # If there are no more lines
        break                          #     leave the loop

    if count == 100:
        break

    # Now process the line we've just read
    parts = theline.split(',')
    longitude = parts[0].strip()
    latitude = parts[1].strip()

    dictionary = {}
    dictionary["longitude"] = float(longitude)
    dictionary["latitude"] = float(latitude)
    jsonlist.append(dictionary)
    count += 1

mynewhandle.close()

with open('data.txt', 'w') as outfile:
    json.dump(jsonlist, outfile, indent=4, separators=(',', ': '))
outfile.close()
