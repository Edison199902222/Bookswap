class Solution:
    # @param nuts: a list of integers
    # @param bolts: a list of integers
    # @param compare: a instance of Comparator
    # @return: nothing
    def sortNutsAndBolts(self, nuts, bolts, compare):
        # write your code here
        self.quick_sort(nuts, bolts, 0, len(nuts) - 1, compare)

    def quick_sort(self, nums1, nums2, start, end, compare):
        if start < end:
            index = self.partition(nums1, nums2[(start + end) // 2], compare, start, end)
            self.partition(nums2, nums1[index], compare, start, end)
            self.quick_sort(nums1, nums2, start, index - 1, compare)
            self.quick_sort(nums1, nums2, index + 1, end, compare)

    def partition(self, nuts, pivot, compare, start, end):
        if start >= end:
            return
        for i in range(len(nuts)):
            if nuts[i] == pivot:
                nuts[i], nuts[end] = nuts[end], nuts[i]
                break
        left = start
        right = end - 1
        while left <= right:
            while left <= right:
                while left <= right and nuts[left] <= pivot:
                    left += 1
                while left <= right and nuts[right] >= pivot:
                    right -= 1
                if left < right:
                    self.swap(nuts, left, right)
        self.swap(nuts, left, end)
        return left

    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]

def main():
    solution = Solution()
    list1 = ["ab", "bc", "dd", "gg"]
    list2 = ["dd", "gg", "ab", "bc"]
    solution.sortNutsAndBolts(list1,list2,1)
    print(list1)
    print(list2)
main()
