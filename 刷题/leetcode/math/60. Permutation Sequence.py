class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [i for i in range(1, n + 1)]
        # 先把所有阶层算出来
        Fac = [1]
        for i in range(1, n):
            Fac.append(Fac[-1] * i)
        result = ""
        k -= 1
        for i in range(n):
            # 算出 低位全排列后 当前位比自己小的有几个数
            m = k // Fac[n - i - 1]
            # 低位全排之后，当前位还需要数多少个
            k = k % Fac[n - i - 1]
            # 加上结果
            result += str(nums[m])
            # 把用掉的数删掉
            nums.remove(nums[m])
        return result
'''
fac[i】的意思 剩余i个数时 可以拥有的组合
比如 fac[2]意思是 前面的数字都确定了 剩下2个数字没确定时 有多少种组合
想法的核心就是 
我们每次从最高位到最低位
每次确定一个数字的组合 
用k % 有多少个以第一位数开头的 组合 来确定 在哪个组合中
比如 数组中又 1 2 3 4 可以选择
那么 我们就有 以1 为开头的 以 2 为开头 以 3 为开头 以4 为开头
每个开头的总数相等 比如 以1 为开头的组合 = 以 2 为开头 组合
那么我们就用k /  有多少种 不一样开头的组合 
就能知道 k 大概以什么为开头的组合之中
'''