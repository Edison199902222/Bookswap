
'''
首先 为什么return的不是p+1 因为p在最后+1了 会多出一个 p就是不重复的元素的个数
还是双指针
我们用p i 先从元素第三个开始 因为元素第三个是第一个可能无效的位置
如果i 的元素 不和p之前两个元素相等的话 说明 这三个不一样 那么p的位置 就是i（不重复元素）的位置
每一次如果看到不重复元素的话 p和i都会同时往右边走一个
如果相等的话 p会指向重复元素 i会继续走 知道i找到不重复的元素 然后把p的元素变成i的
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:return 0
        p = 2
        for i in range(2,len(nums)):
            if nums[i] != nums[p-2]:
                nums[p] = nums[i]
                p+=1
        return p
