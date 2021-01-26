


'''
C(n,m) = C(n - 1, m - 1) + C(n - 1, m)
'''

def caculate(n, m):
    C = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(m + 1):
        C[0][i] = 0
    for i in range(n + 1):
        C[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            C[i][j] = (C[i - 1][j] + C[i - 1][j - 1])
    return C[n][m]

def main():
    n = 5
    m = 3
    result = caculate(n, m)
    print(result)
main()