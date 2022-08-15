import matplotlib
import matplotlib.pyplot as plt

f1 = [0.9653, 0.9247, 0.9653, 0.9942]
m1 = [0.9471, 0.9411, 0.947, 0.9465]
f2 = [0.9679, 0.9421, 0.971, 0.9942]
m2 = [0.9472, 0.9406, 0.9471, 0.9474]
f3 = [0.9637, 0.9479, 0.971, 0.9942]
m3 = [0.9475, 0.9412, 0.9476, 0.9475]

y = ["A", "B", "C", "D"]


p1 = plt.plot(y, f1, marker='o', color='r', label='Fourclass-single', linewidth=0.7)
p2 = plt.plot(y, m1,':', marker='v', color='r', label='Mnist-single', linewidth=0.7)
p3 = plt.plot(y, f2, marker='o', color='k', label='Fourclass-Half', linewidth=0.7)
p4 = plt.plot(y, m2,':', marker='v', color='k', label='Mnist-Half',linewidth=0.7)
p5 = plt.plot(y, f3,marker='o', color='g', label='Fourclass-Bfloat16',linewidth=0.7)
p6 = plt.plot(y, m3, ':',marker='v', color='g', label='Mnist-Bfloat16',linewidth=0.7)
plt.legend() # 显示图例，即每条线对应 label 中的内容
plt.show() # 显示图形
