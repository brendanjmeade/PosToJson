import csv
import datetime
import json
import os
import time
import numpy as np

# Get all .pos file names in current directory
base_path_name = os.getcwd() + '/'
all_files = os.listdir(base_path_name)
file_names = [_ for _ in all_files if _.endswith('.pos')]
file_names.sort()

data = []
for file_name in file_names:
    print file_name
    data_dict = {}
    year = []
    month = []
    day = []
    latitude = []
    longitude = []
    unixtime = []
    file_stream = open(file_name, 'r')

    for i in range(37): # Skip header lines
        file_stream.next()

    for line in file_stream:
        year.append(int(line[1:5]))
        month.append(int(line[5:7]))
        day.append(int(line[7:9]))
        latitude.append(float(line[125:125+14]))
        longitude.append(float(line[141:141+15]) - 360.0)

        # Convert YYYYMMDD to Unix time
        d = datetime.date(year[-1], month[-1], day[-1])
        unixtime.append(time.mktime(d.timetuple()))

    # Package everything in one dictionary
    data_dict['start'] = unixtime[0]
    data_dict['lat'] = latitude
    data_dict['lon'] = longitude
    data_dict['name'] = file_name[0:4]
    data.append(data_dict)
    file_stream.close()

# Write to .json
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
