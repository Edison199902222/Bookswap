"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
'''
先用字典 
去复制所有的node  并且对应原来的node
然后 再扫一遍 把next 跟 random 设置好 用字典
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        graph = {}
        node = head
        # 复制并创建 对应的新node
        while node is not None:
            if node not in graph:
                graph[node] = Node(node.val)
            node = node.next
        # 复制next 跟 random
        for cur in graph:
            if cur.next:
                graph[cur].next = graph[cur.next]
            if cur.random:
                graph[cur].random = graph[cur.random]
        return graph[head]
