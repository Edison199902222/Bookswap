'''
想法：每一次把max_reach记下来 （这是全局最大）
然后 reach是当前可以到的最大步数（上一个最大能做到的）
每次当我们走到 比 reach的时候 就必须要一次跳跃了 step+1 并且把reach更新成max reach

'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_reach = 0
        reach = 0
        step = 0
        for i in range(len(nums)):
            if i > reach:
                reach = max_reach
                step += 1
            max_reach = max(max_reach, i + nums[i])
        return step

if __name__ == "__main__":
    solution = Solution()
    print(solution.jump([2]))