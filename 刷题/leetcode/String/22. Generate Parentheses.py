class Solution:
    def generateParenthesis(self, n: int) :
        self.list = []
        self.helper(0,0,n,"")
        return self.list
    def helper(self,left,right,n,result):
        if left == n and right == n:
            self.list.append(result)
            return
        if left < n:
            self.helper (left+1,right,n,result+"(")
        if right < n and right < left:
            self.helper (left,right+1,n,result + ")")
class Solution2:
    def generateParenthesis(self, n: int) :
        self.result = []
        self.dfs(n,n,"")
        return self.result
    def dfs(self, left, right, path):
        if left == 0 and right == 0:
            self.result.append(path)
            return
        if left > 0:
            self.dfs(left - 1, right, path + "(")
        if right > 0 and right > left:
            self.dfs(left, right - 1, path + ")")
'''
首先 条件是 当左右括号都等于0的时候 我们就可以添加进list中
然后 首先添加左括号 
右括号 只有当左括号数量 大于 右括号时 才可以添加！ 因为 ）（ 这样是不合法的
'''
if __name__ == "__main__":
    solution = Solution2()
    print(solution.generateParenthesis(3))