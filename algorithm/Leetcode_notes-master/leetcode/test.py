def decide(nums1, nums2, target):
    i = len(nums1) - 1
    j = 0
    result = float("inf")
    while i >= 0 and j < len(nums2):
        sums = nums1[i] + nums2[j]
        if sums == target:
            return target
        elif sums < target:
            if abs(result - target) > abs(sums - target):
                result = sums
            j += 1
        else:
            if abs(result - target) > abs(sums - target):
                result = sums
            i -= 1
    return result

def main():
    nums1 = [1,2,3,4,5,6]
    nums2 = [-1,0,1,2,3]
    target = 5
    result = decide(nums1, nums2, target)
    print(result)
main()
