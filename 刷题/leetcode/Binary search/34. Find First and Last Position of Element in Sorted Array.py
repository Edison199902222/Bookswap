'''
用两次binary search
第一次binary search 得到index起点
我们要尽可能 往左边靠 所以我们是先check start 是不是等于target
第二个 binary search 尽量往右边靠 所以我们是先check end 是不是等于target
为什么要用start+1 《 end 是因为我们需要一个区间 需要 左边跟右边两个数 所以用这个
为什么start 跟 end始终不-1 +1 是因为mid已经有可能是我们的target了

'''
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1,-1]
        if not nums or len(nums) == 0:return res
        res[0] = self.findfirst(nums,target)
        res[1] = self.findlast(nums,target)
        return res

    def findfirst(self,nums,target):
        start = 0
        end = len(nums)-1
        while start+1 < end:
            mid = (start + end)//2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        return -1
    def findlast(self,nums,target):
        start = 0
        end = len(nums)-1
        while start+1 < end:
            mid = (start + end)//2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        if nums[end] == target:
            return end
        elif nums[start] == target:
            return start
        return -1

if __name__ == "__main__":
    soluiton = Solution()
    list1 = [5,7,7,8,8,10]
    print(soluiton.searchRange(list1,8))