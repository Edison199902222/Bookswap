class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = []
        prev = float("-inf")
        for index, char in enumerate(S):
            if char == C:
                prev = index
            res.append(index - prev)
        prev = float("inf")
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C:
                prev = i
            res[i] = min(res[i], prev - i)
        return res
'''
将字符串按正、逆顺序两次扫描，
第一次扫描计算当前位置字母与前一个目标字母之间的距离，用prev 指向前一个字母
所以 用index  - prev 
后一次扫描计算当前位置字母与后一个字母之间的距离，两者取小即可
所以是 prev - index 因为这是从后往前扫描 prev是后面的目标字母 永远比index大

'''