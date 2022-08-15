'''
先需要定义一个compare函数
这个函数用来比较 a b 组合起来 谁在前面比较好
比如 a = 8 b = 40
那么比较下 肯定是 840比较大
然后用mergesort 去拆开
用merge去合并 并且判断条件是用compare函数进行比较 哪一个在前面比较大
最后返回 合并起来
'''
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = self.merge_sort(nums, 0, len(nums) - 1)
        return str(int("".join(map(str, nums))))

    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)

    def merge_sort(self, nums, l, r):
        if l > r:
            return
        if l == r:
            return [nums[r]]
        mid = l + (r - l) // 2
        left = self.merge_sort(nums, l, mid)
        right = self.merge_sort(nums, mid + 1, r)
        return self.merge(left, right)

    def merge(self, left, right):
        res, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            if self.compare(left[i],right[j]):
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        while i < len(left):
            res.append(left[i])
            i += 1
        while j < len(right):
            res.append(right[j])
            j += 1
        return res
if __name__ == "__main__":
    solution = Solution()
    print(solution.largestNumber([3,30,34,5,9]))