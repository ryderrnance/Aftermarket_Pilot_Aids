import json
import urllib
import time
import requests
import urllib
# # Opening JSON file
# #f = open('getSituation.json', )
#
# # returns JSON object as
# # a dictionary
url = "http://192.168.10.1/getSituation"
# json_url = urllib.urlopen(url)
# datas = json.loads(json_url.read())
#
# print(datas)
############################




#print(r.json())

#####################
# data = json.load(f)


GPS_VALID = 1
IMU_USED = 2
BMP_USED = 4
CAL = 8
LOG = 16

while True:
    r = requests.get(url)
    data = r.json()
    # for i in data.keys():
    #     print(i)
    invalid = 3276.7

    if data['AHRSMagHeading'] == invalid :
        print('AHRSMagHeading is INVALID')
    else:
        print('AHRSMagHeading',data['AHRSMagHeading']%360)

    if data['AHRSGyroHeading'] == invalid:
        print('AHRSGyroHeading = INVALID')
    else:
        print('AHRSGyroHeading', data['AHRSGyroHeading'] % 360)



    print('BaroPressureAltitude', data['BaroPressureAltitude'])
    print('GPSVerticalAccuracy', data['GPSVerticalAccuracy'] , 'Ft')
    print('GPSAltitudeMSL', data['GPSAltitudeMSL'], 'MSL')
    print('GPSVerticalSpeed', data['GPSVerticalSpeed'])
    print('BaroVerticalSpeed', data['BaroVerticalSpeed'])

    print('######################################################')



    # Closing file
    #f.close()
    time.sleep(2)