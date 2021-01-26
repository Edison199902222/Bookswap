"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal, None)
            head.next = head
            return head
        if not head.next:
            head.next = Node(insertVal, head)
            return head
        cur = head
        # 正着看，cur
        while True:
            if cur.val <= insertVal <= cur.next.val:
                cur.next = Node(insertVal, cur.next)
                return head
            # if current val > next node's val
            # Insert only if current val <= insertVal or insertVal <= next node's val
            if cur.val > cur.next.val:
                # 如果value 大于当前值
                if insertVal >= cur.val or insertVal <= cur.next.val:
                    cur.next = Node(insertVal, cur.next)
                    return head
            cur = cur.next
            # When all elements had same value
            if cur == head:
                cur.next = Node(insertVal, cur.next)
                return head
