# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
分成两个list
如果head 值小于x 那就把这个node 连接到第一个list
如果大于 那么连接到第二个list
然后把第二个大于x的list 把尾部设置成none
最后把两个list连接起来
'''
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)

        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l2.next = None
        l1.next = h2.next
        return h1.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        l1 = cur_l1 = ListNode(0)
        l2 = cur_l2 = ListNode(0)
        while head:
            if head.val < x:
                cur_l1.next = head
                cur_l1 = cur_l1.next
                head = head.next
                cur_l1.next = None
            else:
                cur_l2.next = head
                cur_l2 = cur_l2.next
                head = head.next
                cur_l2.next = None

        cur_l1.next = l2.next
        return l1.next