import csv
import numpy as npp

csvd = open("temp1.csv", "w")
writer = csv.writer(csvd)

npp.set_printoptions(suppress=True)
W1 = npp.random.randn(4, 2) * npp.sqrt(2 / 2)
b1 = npp.zeros((4, 1))
writer.writerow(W1)

csvd2 = open("temp2.csv", "w")
writer = csv.writer(csvd2)
writer.writerow(b1)

W2 = npp.random.randn(2, 4) * npp.sqrt(2 / 4)
b2 = npp.zeros((2, 1))
print(W2)
csvd3 = open("temp3.csv", "w")
writer = csv.writer(csvd3)
writer.writerow(W2)

csvd4= open("temp4.csv", "w")
writer = csv.writer(csvd4)
writer.writerow(b2)

