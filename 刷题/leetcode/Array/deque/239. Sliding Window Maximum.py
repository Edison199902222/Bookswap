'''
使用双向队列 维护一个单调递减
这样 队列的首位就是我们的最大值
一个队列用来存储window的下标 一个list用来储存最大值
每次滑动 我们需要做的是检查 这个window的最大值有没有过期 输出最大值
如果新进来的数字比最大数小 可以直接添加到队列尾部 如果比队列中最大的数大 则清空
'''
import collections


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        deque = collections.deque()
        result = []
        for right in range(len(nums)):
            if right >= k and right - k >= deque[0]:
                deque.popleft()
            while deque and nums[right] > nums[deque[-1]]:
                deque.pop()
            deque.append(right)
            if right >= k - 1:
                result.append(nums[deque[0]])
        return result

if __name__ == '__main__':
    solution = Solution()
    list = [1,-1]
    print(solution.maxSlidingWindow(list,1))