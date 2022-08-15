# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
有一点像数学题
规律就是 如果有环的话
那么让slow 继续走 head从头开始走 他们相遇的地方就是入口

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        # 首先，头结点到入环结点的距离为a，入环结点到相遇结点的距离为b，相遇结点到入环结点的距离为c。
        # 然后，当f以s的两倍速度前进并和s相遇时，f走过的距离是s的两倍，即有等式：a+b+c+b = 2(a+b) ，可以得出 a = c
        # 所以说，让fast和slow分别从相遇结点和头结点同时同步长出发，他们的相遇结点就是入环结点
        fast = slow = head
        # 保证不为空
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 如果相遇
            if slow == fast:
                # head从头开始走， 因为此时 slow 到 环起始点 的距离 = head 到 环起始点的距离
                while head:
                    if head == slow:
                        return head
                    head = head.next
                    slow = slow.next
        return None