import csv

stationsfile = 'stations.csv'

with open(stationsfile, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print row[0]
