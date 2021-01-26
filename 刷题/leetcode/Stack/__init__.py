

def solve(nums):
    stack = []
    result = [-1 for i in range(len(nums))]
    for i in range(len(nums) -1, -1, -1):
        if not stack:
            stack.append(i)
        elif nums[i] > nums[stack[-1]]:
            stack.append(i)
        elif nums[i] < nums[stack[-1]]:
            index = binary_search(nums, stack, nums[i])
            result[i] = index
    return result


def binary_search(nums, stack, target):
    left = 0
    right = len(stack) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[stack[mid]] > target:
            right = mid
        else:
            left = mid
    if nums[stack[left]] > target:
        return stack[left]
    return stack[right]

def main():
    list = [21,5,6,56,88,52]
    list2 = [88,12,1,15,16,9]
    result = solve(list)
    result2 = solve(list2)
    print(result)
    print(result2)
main()