import csv
with open("city.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
         print(row)