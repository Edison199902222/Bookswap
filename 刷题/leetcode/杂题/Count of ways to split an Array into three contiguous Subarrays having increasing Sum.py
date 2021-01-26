

'''
Given an array arr[] consisting of non-negative integers,
the task is to find the number of ways to split the array into three non-empty contiguous subarrays such that
heir respective sum of elements are in increasing order.
Input: arr[] = {2, 3, 1, 7}
Output: 2
Explanation:
{{2}, {3, 1}, {7}}, {{2}, {3}, {1, 7}} are the possible splits.

Input: arr[] = {1, 2, 0}
Output: 0
'''


def findCount(arr):
    if len(arr) < 3:
        return 0
    n = len(arr)
    prefix_sum = [0 for i in range(n)]
    prefix_sum[0] = arr[0]
    for i in range(1, n):
        prefix_sum[i] += prefix_sum[i - 1] + arr[i]
    result = 0
    p1 = 0
    p2 = 1
    while p1 < n - 2:
        while p2 < n and (p1 >= p2 or prefix_sum[p2] - prefix_sum[p1] < prefix_sum[p1]):
            p2 += 1
        if p2 < n - 1:
            p3 = binary_search(prefix_sum, p2, p1)
            print(p1,p2,p3)
            if p3 != -1:
                result += p3 - p2 + 1
        p1 += 1
    return result

def binary_search(arr,p2, p1):
    left = p2
    right = len(arr) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if arr[-1] - arr[mid] >= arr[mid] - arr[p1]:
            left = mid
        else:
            right = mid
    if arr[-1] - arr[right] >= arr[right] - arr[p1] and right != len(arr) - 1:
        return right
    if arr[-1] - arr[left] >= arr[left] - arr[p1] and left != len(arr) - 1:
        return left
    return - 1


def find(arr):
    if len(arr) < 3:
        return 0
    n = len(arr)
    prefix_sum = [0 for i in range(n)]
    prefix_sum[0] = arr[0]
    for i in range(1, n):
        prefix_sum[i] += prefix_sum[i - 1] + arr[i]
    result = 0
    for i in range(n):
        first_sum = prefix_sum[i]
        for j in range(i + 1, n - 1):
            second_sum = prefix_sum[j] - prefix_sum[i]
            thrid_sum = prefix_sum[-1] - prefix_sum[j]
            if first_sum <= second_sum <= thrid_sum:
                result += 1
                print(i,j)
    return result
# Driver code
arr = [1,2,3,0,0,10,0,0,6]






n = len(arr)

print(findCount(arr))

# This code is contributed by Stream_Cipher




