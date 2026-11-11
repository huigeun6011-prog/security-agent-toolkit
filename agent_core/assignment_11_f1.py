import csv

with open("gichan_input.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    count = 0
    for row in reader:
        if row["result"] == "FAIL":
            count += 1
    print(count)