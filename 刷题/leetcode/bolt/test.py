import numpy as np
from scipy.linalg import inv
from scipy.optimize import lsq_linear
import matplotlib.pyplot as plt


A = np.array(
    [[1,0],
     [1,-1],
     [1,-2],
     [1,-3]]
)



b = np.array([128000, 122000, 118000, 112000])
# b = np.array([158000, 141000, 121000, 109000])

sol = lsq_linear(A, np.log(b)).x
print(lsq_linear(A, np.log(b)).x)

print(np.exp(sol[0]), 1 / (sol[1]))