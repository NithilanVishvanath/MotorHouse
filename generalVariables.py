import csv
with open('bikeproj.csv','r') as motorhouse:
    rows = csv.reader(motorhouse)
    specs = (list(rows))[0]