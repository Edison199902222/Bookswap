class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for i in range(amount + 1)]
        dp[0] = 0
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    # 完全背包，因为当前物品可以选无数次，所以在考虑“加选一件第i种物品”这种策略时，却正需要一个可能已选入第i种物品的子结果f[i][v-c[i]]
                    # 有可能本层i 之前的j - coin[i - 1] 选过了当前的物品，我们也可以选
                    # 但01背包不能，因为只能选一次！！
                    dp[j] =  min(dp[j], dp[j - coins[i - 1]] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
'''
完全背包问题， 内循环正序
dp[i][j]意思是 前i个硬币 能凑成amount 为j 的number 是几
初始化最大值
然后 枚举前i个物品
枚举amount 大小
与 自己的初始化值 跟 j - 当前coin 的值 + 1 取最小值
如果结束后，还是为初始值，说明不能凑成这样的amount 
'''


if __name__ =='__main__':
    solution = Solution()
    print(solution.coinChange([2],3))