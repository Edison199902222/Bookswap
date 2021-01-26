'''
我们需要借助dfs
每次加一个字母 并且 到下一个index中 再去添加字母 然后如果path的长度跟digitis 长度相等 说明我们已经添加完成

'''

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        res = []
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        self.dfs(digits, 0, "", res, dic)
        return res

    def dfs(self, digits, index, path, res, dic):
        if len(digits) == len(path):
            res.append(path)
            return
        for i in dic[digits[index]]:
            self.dfs(digits,index+1,path+i,res,dic)
