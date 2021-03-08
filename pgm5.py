import csv
fd=["slno","name","city"]
with open("city.csv","w") as file:
    w=csv.DictWriter(file,fieldnames=fd)
    w.writeheader()
    w.writerow({"slno":1,"name":"ccc","city":"kakkattil"})