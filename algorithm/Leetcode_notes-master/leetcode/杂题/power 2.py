import collections


def find_x(arr):
    dic = collections.defaultdict(int)
    result = 0
    for i in range(len(arr)):
        dic[arr[i]] += 1
        cur = 1
        for j in range(32):
            temp = cur << j
            if temp - arr[i] in dic:
                result += dic[temp - arr[i]]
    return result


def main():
    arr = [-2,-1,0,1,2]
    result = find_x(arr)
    print(result)


main()
