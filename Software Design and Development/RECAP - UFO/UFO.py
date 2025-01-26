# RECAP - UFO
# Original task by Mr Neil, adapted by Mr Simpson

import csv
thisDate = []
country = []
location = []
shape = []
description = []
filePath = 'Software Design and Development/RECAP - UFO/'

# -------------------------------------------------- DO NOT ALTER -----
def importFile():
    with open(filePath+'ufo_sighting.csv','r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            thisDate.append(row[0])
            country.append(row[1])
            location.append(row[2])
            shape.append(row[5])
            description.append(row[6])
    return thisDate, country, location, shape, description
# -------------------------------------------------- DO NOT ALTER -----

thisDate, country, location, shape, description = importFile()