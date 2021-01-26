# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if not nestedList:
            return 0
        return self.dfs(nestedList, 1)

    def dfs(self, nestedList, deapth):
        result = 0
        for num in nestedList:
            if num.isInteger():
                result += num.getInteger() * deapth
            else:
                result += self.dfs(num.getList(), deapth + 1)
        return result
'''
先创建dfs函数
对于每一层递归 我们要遍历这一层所有的数组或者数字
然后判断 它是数字的话 我们直接加进结果
不是的话 我们继续递归 并且deapth + 1
'''

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        if len(nestedList) == 0:
            return 0
        stack = []
        sums = 0
        for i in nestedList:
            stack.append((i, 1))
        while stack:
            node, depth = stack.pop()
            if node.isInteger():
                sums += depth * node.getInteger()
            else:
                for num in node.getList():
                    stack.append((num, depth + 1))
        return sums