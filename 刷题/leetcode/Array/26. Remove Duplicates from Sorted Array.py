
'''

按照这个思路呢，又可以衍生出解决类似需求的通用方式：双指针技巧。具体一点说，应该是快慢指针。

我们让慢指针slow走左后面，快指针fast走在前面探路，找到一个不重复的元素就告诉slow并让slow前进一步。

这样当fast指针遍历完整个数组nums后，nums[0..slow]就是不重复元素，之后的所有元素都是重复元素。
https://cloud.tencent.com/developer/article/1513979
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:return 0
        count = 0
        for i in range(1,len(nums)):
            if nums[count]!=nums[i]:
                count+=1
                nums[count] = nums[i]
        return count+1



