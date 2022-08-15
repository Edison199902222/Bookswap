class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.memo = {}
        return self.dfs(s)

    def dfs(self, s):
        # 递归过程中，只有++才能变成--， 所以每一步状态和空间都会越来越小，所以base case 可以没有
        if s in self.memo:
            return self.memo[s]
        flag = False
        # 遍历s， 遇到两个++， 就尝试去变成--， 然后递归下去
        # 如果递归的状态返回的是false， 说明我们选择的这一步，对手会输，我们这一层状态就是true
        # 只要有一个能使得对手的状态是false，那我们就break
        for i in range(len(s) - 1):
            if s[i] == s[i + 1] == "+":
                temp = s[:i] + "-" + "-" + s[i + 2:]
                current_flag = self.dfs(temp)
                if current_flag == False:
                    flag = True
                    break
        self.memo[s] = flag
        return flag