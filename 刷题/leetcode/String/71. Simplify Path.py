class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for item in path.split("/"):
            if item not in [".", "..", ""]:
                stack.append(item)
            if stack and item == "..":
                stack.pop()
        return "/" + "/".join(stack)
'''
题目意思是 对于每一个path 我们先 split "/" 但是里面会有 ""
如果遇到 点 就不添加
如果遇到 两个点 并且不是空 就要从 stack中pop出去
最后返回 stack中的元素 
'''