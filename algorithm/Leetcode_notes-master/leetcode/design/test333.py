import csv
import random

csvd = open("temp5.csv", "w")
writer = csv.writer(csvd)
for i in range(1000):
    temp = []
    for x in range(2):
        cur = ""
        mid = bin(random.randint(1, 254))
        cur += str(random.randint(0, 1))
        end = ""
        for j in range(23):
            end += str(random.randint(0, 1))
        cur += str(mid).replace("0b", "")
        cur += end
        temp.append(cur + "\t")
    writer.writerow(temp)
