# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
1 -> 2 -> 3 -> 4
想delete 2
那么我们就把2 变成 3。 1 -> 3 -> 3 -> 4
然后在把2 节点 连接到4 就好  1 -> 3 -> 4
'''
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        cur = node
        if cur.next is not None:
            cur.val = cur.next.val
            cur.next = cur.next.next
