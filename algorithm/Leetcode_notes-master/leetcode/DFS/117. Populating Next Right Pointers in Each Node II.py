
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
'''
这道题看答案看了很久
难点其实主要是 需要提前把第二层知道
head是下一层的第一个节点 prev负责把下一层连接起来
cur 就是这一层的node 
'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:return root
        head = None
        prev = None
        cur = root
        while cur!=None:
            while cur!=None:
                if cur.left!=None:
                    if head == None:
                        head = cur.left
                        prev = cur.left
                    else:
                        prev.next = cur.left
                        prev = prev.next
                if cur.right!=None:
                    if head == None:
                        head = cur.right
                        prev = cur.right
                    else:
                        prev.next = cur.right
                        prev = prev.next
                cur = cur.next
            cur = head
            head = None
            prev = None
        return root


