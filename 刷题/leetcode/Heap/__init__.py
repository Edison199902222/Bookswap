def findCount(arr, n):
    if n < 3:
        return 0
    prefix_sum = [0 for i in range(n)]
    prefix_sum[0] = arr[0]
    for i in range(1, n):
        prefix_sum[i] += prefix_sum[i - 1] + arr[i]
    # 指向第一个区间结束的地方
    p0 = 0
    # 指向第二个区间结束的地方
    p1 = 1
    result = 0
    while p0 < n - 2:
        # 当第二个区间小于第二个区间，第二个区间 ++
        while p1 < n - 1 and prefix_sum[p1] - prefix_sum[p0] < prefix_sum[p0]:
            p1 += 1
        if p1 < n - 1:
            p2 = bs(prefix_sum, p1, p0)
            if p2 != -1:
                result += (p2 - p1 + 1)
        p0 += 1
    return result

def bs(arr, p1, p0):
    left = p1
    right = len(arr) - 2
    while left + 1 < right:
        mid = (left + right) // 2
        sums = arr[mid] - arr[p0]
        if sums < arr[-1] - arr[mid]:
            left = mid
        right = mid
    if arr[right] - arr[p0] <= arr[-1] - arr[right]:
        return right
    if arr[left] - arr[p0] <= arr[-1] - arr[left]:
        return left
    return -1

def findCount2(arr, n):
    if n < 3:
        return 0
    prefix_sum = [0 for i in range(n)]
    prefix_sum[0] = arr[0]
    for i in range(1, n):
        prefix_sum[i] += prefix_sum[i - 1] + arr[i]
    suffix_sum = [0 for i in range(n)]
    suffix_sum[-1] = arr[-1]
    for i in range(n - 2, -1, -1):
        suffix_sum[i] += suffix_sum[i + 1] + arr[i]
    result = 0
    cur_sum = 0
    p1 = 1
    p2 = 1
    while p2 < n and p1 < n - 1:
        while p1 < n - 1 and cur_sum < prefix_sum[p1 - 1]:
            cur_sum += arr[p2]
            p2 += 1
        while p2 < n and cur_sum <= suffix_sum[p2]:
            result += 1
            print(p1,p2)
            cur_sum += arr[p2]
            p2 += 1
        cur_sum -= arr[p1]
        p1 += 1
    return result

# Driver code
arr = [0,0,0,0,0]
n = len(arr)

print(findCount(arr, n))
print(findCount2(arr, n))