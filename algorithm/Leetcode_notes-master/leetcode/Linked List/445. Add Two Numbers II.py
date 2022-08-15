# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node_l1 = l1
        node_l2 = l2
        new_head_l1 = self.reverse(node_l1)
        new_head_l2 = self.reverse(node_l2)
        carry = 0
        dummy = cur = ListNode(0)
        while new_head_l1 or new_head_l2 or carry:
            if new_head_l1:
                carry += new_head_l1.val
                new_head_l1 = new_head_l1.next
            if new_head_l2:
                carry += new_head_l2.val
                new_head_l2 = new_head_l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
        result = self.reverse(dummy.next)
        return result

    def reverse(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = 0, 0
        while l1 or l2:
            if l1:
                s1 = s1 * 10 + l1.val
                l1 = l1.next
            if l2:
                s2 = s2 * 10 + l2.val
                l2 = l2.next
        s3 = str(s1 + s2)
        dummy = cur = ListNode(s3[0])
        for i in range(1, len(s3)):
            cur.next = ListNode(int(s3[i]))
            cur = cur.next
        return dummy

