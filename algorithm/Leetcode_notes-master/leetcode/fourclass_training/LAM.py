from decimal import Decimal

'''''
  把一个带小数的二进制数n转换成十进制
  小数点后面保留pre位小数
'''
'''
  string_number1 = str(n) #number1 表示二进制数，number2表示十进制数
  decimal = 0 #小数部分化成二进制后的值
  flag = False
  for i in string_number1: #判断是否含小数部分
    if i == '.' or i == 'e':
      flag = True
      break
    
    if flag: #若二进制数含有小数部分
    else: #若二进制数只有整数部分
    return int(string_number1, 2)#若只有整数部分
'''
def bTod(n, pre=10):
    string_number1 = f'{n:.24f}'
    decimal = 0
    string_integer, string_decimal = string_number1.split('.') #分离整数部分和小数部分
    for i in range(len(string_decimal)):
        decimal += 2**(-i-1)*int(string_decimal[i]) #小数部分化成二进制
    number2 = int(str(int(string_integer, 2))) + decimal
    return round(number2, pre)



def dTob(n, pre=24):
    string_number1 = f'{n:.30f}'  # in case scientific notation 防止科学计数形式的输入
    string_integer, string_decimal = string_number1.split('.')  # 分离整数部分和小数部分
    integer = int(string_integer)
    decimal = Decimal(string_number1) - integer
    l1 = [0, 1]
    l2 = []
    decimal_convert = ""
    while True:
        if integer == 0: break
        x, y = divmod(integer, 2)  # x为商，y为余数
        l2.append(y)
        integer = x
    string_integer = ''.join([str(j) for j in l2[::-1]])  # 整数部分转换成二进制
    i = 0
    while decimal != 0 and i < pre * 5:
        result = int(decimal * 2)
        decimal = decimal * 2 - result
        decimal_convert = decimal_convert + str(result)
        i = i + 1
    string_number2 = string_integer + '.' + decimal_convert
    # print(string_number2)
    return float(string_number2)
'''''
    把一个带小数的十进制数n转换成二进制
    小数点后面保留pre位小数
    '''
'''
    string_number1 = str(n) # number1 表示十进制数，number2表示二进制数
    flag = False
    for i in string_number1:  # 判断是否含小数部分
        if i == '.' or i == 'e':
            flag = True
            break

    if flag:


    else:  # 若十进制只有整数部分
        l1 = [0, 1]
        l2 = []
        while True:
            if n == 0: break
            x, y = divmod(n, 2)  # x为商，y为余数
            l2.append(y)
            n = x
        string_number = ''.join([str(j) for j in l2[::-1]])
        return int(string_number)

    ### return float or int, could be scientific notation
'''

def binary_float_exponent(N_bin):
    if isinstance(N_bin, int):
        N_exp = len(str(N_bin)) - 1  # A MSB index; decimal
    else:
        # show all precision of float number
        str_N_bin = f'{N_bin:.24f}'
        str_integer, str_fraction = str_N_bin.split('.')  # 分离整数部分和小数部分
        if str_integer != '0': #exponent >= 0
            N_exp = len(str_integer) - 1
        elif str_integer == '0': #exponent < 0
            index = -1
            for i in range(len(str_fraction)):
                if str_fraction[i] == "1":
                    index = i + 1
                    break
            N_exp = -index

    return N_exp #could be positive or negative

def difference_compare(N):
    #binary format of N
    N_bin = dTob(N) #return float or int, could be scientific notation
    #calculate exponent
    N_exp = binary_float_exponent(N_bin)
    N_frac = float(N_bin / 10 ** N_exp)  # N_frac is the fraction part of binary A

    return N_exp, N_frac

def remove_sign(signed_N):
    abs_N = abs(signed_N)
    if signed_N < 0:
        N_sign = 'negative'
    else:
        N_sign = 'positive'

    return abs_N, N_sign #abs_N is float or int, could be scientific notation

def approx_multiplication(signed_A,signed_B):
    if signed_A == 0 or signed_B == 0:
        P_approx = 0
    else:
        #remove sign of the operands
        abs_A, A_sign = remove_sign(signed_A)
        abs_B, B_sign = remove_sign(signed_B)

        A_exp, A_frac = difference_compare(abs_A)
        B_exp, B_frac = difference_compare(abs_B)

        #print(A_exp, A_frac, B_exp, B_frac)
        P_exp = A_exp + B_exp #decimal
        P_frac = bTod(A_frac) + bTod(B_frac) - 1 #decimal
        #print(bTod(A_frac),bTod(B_frac))
        #print(P_frac)
        P_approx = P_frac * (2 ** P_exp)
        #print(P_approx)
        if A_sign == B_sign:
            P_approx = P_approx
        else:
            P_approx = -P_approx

    return P_approx

