import csv
with open("city.csv","r") as file:
    r=csv.DictReader(file)
    for row in r:
        print(row["slno"],row["name"],row["city"])
