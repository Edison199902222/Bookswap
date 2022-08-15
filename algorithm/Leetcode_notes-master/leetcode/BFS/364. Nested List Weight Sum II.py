# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
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
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        res = 0
        level_res = 0
        queue = nestedList
        while queue:
            level_queue = []
            for node in queue:
                if node.isInteger():
                    level_res += node.getInteger()
                else:
                    for y in node.getList():
                        level_queue.append(y)
            res += level_res
            queue = level_queue
        return res

'''
对于每一层
level quenue 记录下一层的list
level_res记录每一层的值 跟之前的层的值
我们判断 这一层如果有数字的话 我们直接把数字加进level res之中
如果不是数字 那么 我们对list里面的每个元素 加入进level quenue之中
然后我们再把 level res加入 result中
我们通过不断加level result 进 result中 这样我们即可以把前几层的值不断累加 也就是实现了数字乘相应的深度
然后进入下一层之中
'''