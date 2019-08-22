import csv



mas = "example.csv"


with open(mas) as file1:
    csv_reader = csv.reader(file1, delimiter=',')
    line = 0
    top = []
    bottom = []
    for row in csv_reader:
        if line == 0:
            top = row
            line += 1
        elif line == 1:
            bottom = row
            line += 1
    kam = zip(top,bottom)

    for i in kam:
        print(i)
