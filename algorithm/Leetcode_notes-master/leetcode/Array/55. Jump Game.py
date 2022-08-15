'''
想法是：用max_reach这个变量去get到 我们最远可以到达多少 每一次都需要更新最远那个
然后 用loop 遍历 如果当前的index 超出了max_reach的话 说明这个index 我们是不能到达的 所以return false
如果max——number 大于等于这个list长度的话 return True
与jump 2 不一样的事 这道题不一定能到底最后index！！ 所以每次需要check 下一步 是不是能到达 是不是在max——reach 范围之内
'''

class Solution:
    def canJump(self, nums) -> bool:
        if not nums:
            return False
        max_reach = 0
        length = len(nums)
        for i in range(length):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= length - 1:
                return True
        return False