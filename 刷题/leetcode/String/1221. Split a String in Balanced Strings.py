class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        L_count = 0
        R_count = 0
        W_count = 0
        for i in s:
            if i == "L":
                L_count +=1
            else:
                R_count += 1
            if L_count == R_count:
                W_count += 1
        return W_count
'''
遍历string 
发现 l 的话 L count += 1
发现 r 的话 r count += 1
每次检查 l 与 r 是否相等
相等的话 我们的w + 1
'''