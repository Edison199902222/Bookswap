'''
用stack
需要确定subarray 这个的左边边界 与右边边界
从头往前遍历
stack维持 从小到大的顺序
如果发现进得来的数 小于 stack最后一个
那么就用while 一直与stack最后一个 进行对比 并且pop
从后往前遍历
stack维持 从大到小顺序
如果发现进来的数 大于 stack最后一个
那么就用while 一直与stack最后一个 进行对比 并且pop
'''

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        leftbound,rightbound = len(nums),0
        for i in range(len(nums)):
            while len(stack) != 0 and nums[i] < nums[stack[-1]]:
                leftbound = min(leftbound,stack.pop())
            stack.append(i)
        stack = []
        for i in range(len(nums)-1,-1,-1):
            while len(stack)!= 0 and nums[i] > nums[stack[-1]]:
                rightbound = max(rightbound,stack.pop())
            stack.append(i)
        if rightbound - leftbound > 0 :
            return rightbound - leftbound + 1
        if rightbound - leftbound <= 0:
            return 0
if __name__ == "__main__":
    solution = Solution()
    print(solution.findUnsortedSubarray([1,3,2,3,3]))