#test_csv1.py
import csv

with open('test.csv' , 'rb', encoding="utf-8") as csvfile:
    members = csv.reader(csvfile, delimiter=",")
    for row in members:
        print( ','.join(row) )


    