import collections


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        nodes = preorder.split(",")
        for node in nodes:
            stack.append(node)
            # 证明是有叶子节点了
            while len(stack) >= 3 and stack[-1] == "#" and stack[-2] == "#":
                stack.pop()
                stack.pop()
                # 两个# 证明必须要有一个非 空的节点，不然是false
                if stack.pop() == "#":
                    return False
                stack.append("#")
        return len(stack) == 1 and stack[0] == "#"
'''
自下向上来判断
只要出现 stack 最后两个 是 #， 说明一个叶子节点出现
通过判断叶子 来延伸到整个tree
'''