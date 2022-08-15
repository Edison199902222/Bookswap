import csv
import numpy as npp
import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_csv("fourclass.csv", header = None)
df2 = pd.read_csv("diabetes_testResult.csv", header = None)

plt.scatter(df1[0], df1[1], c=df1[0]>df1[1], cmap="Set1")
plt.scatter(df2[0], df2[1], c=df2[0]>df2[1], cmap="Set3")
plt.show()
