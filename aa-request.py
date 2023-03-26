import requests

# Notes: needs valid cookie in request header.

url = (
    "https://www.aa.com/seats/dialog" +
    "?legs[0].flightNumber=2430" +
    "&legs[0].departureMonth=3" +
    "&legs[0].departureDay=27" +
    "&legs[0].origin=CLE" +
    "&legs[0].destination=CLT" +
    "&legs[0].aircraft=320" +
    "&legs[0].wifi=true" +
    "&legs[0].highSpeedWifi=true" +
    "&legs[0].power=true" +
    "&legs[0].carrier=AA" +
    "&_=1679862637525" # this appears to auto-increment
)

header = {}
ignore_params = []
with open('header.txt') as headerfile:
    for line in headerfile.readlines():
        if ':' in line:
            key, value = line.split(':', maxsplit=1)
            if key not in ignore_params:
                header[key.strip()] = value.strip()

resp = requests.get(url, headers=header)
print(resp.content)
