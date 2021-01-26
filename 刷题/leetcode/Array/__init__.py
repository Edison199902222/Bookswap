
import numpy as np
def caculate(a,b,c,d):
    result_fist = [[a**2,a*b,a*c,a*d],[a*b, b**2, b*c, b*d],[a*c, b*c, c**2, c*d],[a*d, b*d, c*d,d**2]]
    np.set_printoptions(suppress=True)
    return np.array(result_fist)
def main():
    a = caculate(0.2,0.9,0.4,1.3)
    b = caculate(-0.37,-0.56,-0.74,4.26)
    c = caculate(-0.71,0,0.71,0.71)
    d = caculate(-0.32,0.81,-0.49,-0.47)
    e = caculate(-0.58,0.58,-0.58,1.16)
    f = caculate(0.24,0.84,-0.48,-2.28)
    temp = a + b + c + d + e + f
    g = caculate(0.2,-0.9,0.4,1.3)
    h = caculate(-0.37,-0.56,-0.74,4.26)
    j = caculate(-0.65,0.65,-0.39,1.69)
    k = caculate(0.41,-0.41,-0.82,0)
    temp2 = g + h + j + k
    print(temp)
    print("    ")
    print(temp2)
    result = temp + temp2
    print(result)





main()
