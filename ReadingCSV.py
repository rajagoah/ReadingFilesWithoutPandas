import csv


with open('/Users/aakarsh.rajagopalan/Personal documents/Python projects/CON data set/CON-MP-All statuses 2-13 db2.csv', "r") as file:
    my_reader = csv.reader(file, delimiter=',')
    for row in my_reader:
        print(row, "\n")