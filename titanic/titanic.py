import csv
lst=[]
total_age=0.0
total = 0
with open('titanic.txt', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row[1] == "1" :
            total += 1
            lst.append(row[5])
for val in lst :
    if val =="" or val == " " :
        val = 0.0
    total_age = total_age + float(val)
avg_age = total_age/total
print("Avg age of survived people:",avg_age)
