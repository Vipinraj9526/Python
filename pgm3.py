import csv
with open("city.csv","w") as file:
    writer=csv.writer(file)
    writer.writerow([1,"max","thrissur"])
    # for row in reader:
    #      print(row)