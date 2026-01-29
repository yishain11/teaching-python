import csv

# read
with open("./data.csv", "r") as f:
    csv_reader = csv.reader(f, delimiter=",")
    for row in csv_reader:
        print(row)

# write
with open("./data.csv", "a", newline="") as f:
    writer = csv.writer(f)
    name = input("enter name ")
    age = input("enter age ")
    addr = input("enter addr ")
    writer.writerow([name, age, addr])
