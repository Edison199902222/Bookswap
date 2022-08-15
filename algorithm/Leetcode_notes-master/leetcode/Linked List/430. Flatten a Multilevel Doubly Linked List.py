"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        self.nodes = []
        self.dfs(head)
        head = self.nodes[0]
        head.child = None
        for i in range(1, len(self.nodes)):
            cur = self.nodes[i]
            prev = self.nodes[i - 1]
            cur.child = None
            cur.prev = prev
            prev.next = cur
        return head

    def dfs(self, node):
        if node is None:
            return
        self.nodes.append(node)
        if node.child:
            self.dfs(node.child)
        if node.next:
            self.dfs(node.next)

'''
用dfs按顺序 把所有的node 放进 nodes中
然后重新链接 整个列表
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # 如果有child， 把当前next设置成child，并且找到child 的next 指针在哪， 把next 连上当前cur 的next， 连上后如果cur 的next不是0的话，也设置prev
        cur = head
        while cur:
            if cur.child:
                # 先把下一个 用 一个指针指向
                cur_next = cur.next
                # 把下一个设置成child， 并且用last 指向child
                last = cur.child
                cur.next = cur.child
                # 把下一个的prev 设置成自己
                cur.next.prev = cur
                # 找到当前child 的尾巴
                while last.next:
                    last = last.next
                # 找到后，连上之前 cur 的下一个
                last.next = cur_next
                # 并且如果下一个不是none 的话， 把下一个设置prev
                if last.next:
                    last.next.prev = last
                cur.child = None
            cur = cur.next
        return head

