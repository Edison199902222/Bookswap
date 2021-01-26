
# 辗转相除法
def gcd(a,b):
    # c 是最大公约数， 如果 a 是 c 的 n 倍
    # b 是 c 的 m 倍，a % b = r， 那么余数 r 也会是 c 的 x 倍
    # 不断缩小 a b， 直到b 等于0， 此时 a 就是最大公约数
    # a % b = r
    if b == 0:
        return a
    return gcd(b, a % b)


def helper(a,b):
    result = []
    gcd_number = []
    length = 0
    a.sort()
    b.sort()
    for i in range(1, len(a)):
        gcd_number.append(gcd(a[i - 1], a[i]))

    min_value = min(min(a), min(b))
    a_new = set(a)
    b_new = set(b)
    for i in range(len(gcd_number)):
        current_gcd = gcd_number[i]
        current_result = [min_value]
        cur_length = 1
        while True:
            if current_result[-1] + current_gcd in a_new or current_result[-1] + current_gcd in b_new:
                current_result.append(current_result[-1] + current_gcd)
                cur_length += 1
                if cur_length > length:
                    length = cur_length
                    result = current_result
            else:
                break
    temp = set(result)
    for i in range(len(a)):
        if a[i] not in temp:
            return 0
    return result





def main():
    a = [4,6,8]
    b = [2,10]
    result = helper(a,b)
    print(result)
main()