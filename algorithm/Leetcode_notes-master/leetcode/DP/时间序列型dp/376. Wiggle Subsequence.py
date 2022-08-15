'''
up[i] 存的是目前为止最长的以第 i 个元素结尾的上升摆动序列的长度。

类似的， down[i] 记录的是目前为止最长的以第 i 个元素结尾的下降摆动序列的长度。

如果 nums[i] > nums[i-1] ，意味着这里在摆动上升，前一个数字肯定处于下降的位置。所以 up[i] = down[i-1] + 1 ， down[i] 与 down[i-1] 保持相同。

如果 nums[i] < nums[i-1] ，意味着这里在摆动下降，前一个数字肯定处于上升的位置。所以 down[i] = up[i-1] + 1 ， up[i]与 up[i−1] 保持不变。

如果 nums[i] == nums[i-1] ，意味着这个元素不会改变任何东西因为它没有摆动。所以 down[i] 与 up[i] 与 down[i-1] 和 up[i−1] 都分别保持不变。

最后，我们可以将 up[-1] 和 down[-1] 中的较大值作为问题的答案.
'''
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 第i轮状态只取决于i - 1 轮的状态
        # 0 上升
        # 1 下降
        if not nums:
            return 0
        n = len(nums)
        dp = [[1] * 2 for i in range(len(nums))]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i][0] = dp[i - 1][1] + 1
                dp[i][1] = dp[i - 1][1]
            elif nums[i] < nums[i - 1]:
                dp[i][1] =  dp[i - 1][0] + 1
                dp[i][0] = dp[i - 1][0]
            # 因为可以删除元素， 所以保持不变
            else:
                dp[i][1] = dp[i - 1][1]
                dp[i][0] = dp[i - 1][0]
        return max(dp[n - 1][0], dp[n - 1][1])


    def wiggleMaxLength(self, nums) -> int:
        n = len(nums)
        if n < 2:
            return n
        up = 1
        down = 1
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                up = down+1
            elif nums[i] < nums[i-1]:
                down = up+1
        return max(up,down)
if __name__ == "__main__":
    solution = Solution()
    print(solution.wiggleMaxLength([1,7,4,9,2,5]))