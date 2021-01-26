# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        stack = []
        result = []
        while head:
            while stack and head.val > stack[-1][1]:
                result[stack.pop()[0]] = head.val
            stack.append([len(result),head.val])
            result.append(0)
            head = head.next
        return result
'''
还是用单调栈
每次进来的node 先与stack之中的val 比较 
如果发现进来的node value 大于stack栈顶的 value 
我们就pop出栈顶元素 然后更新pop元素 的index的 值
然后再把自己添加进stack中
再向result 数组中 添加自己index 的值 也就是 0
'''