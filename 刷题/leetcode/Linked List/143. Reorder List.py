# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
拆分成三个部分去解决
先用findmid  去找到中间node
然后 把list 拆成两个部分
然后把后半部分 反转
然后再进行合并 
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 把 整个链表先分成两个链表
        # 第一个链表是前半部分， 第二个链表是后面的部分， 然后reverse 第二个链表
        # 把第二个链表的node 往第一个链表里面插入
        # 找到中点
        if not head:
            return head
        mid = self.find_mid(head)
        # 找到第二个链表的起点
        l2 = mid.next
        # 断开
        mid.next = None
        # reverse
        l2 = self.reverse(l2)
        l1 = head
        # 插入进去, 条件是l1 and l2 or l2都可以， 最主要看l2,因为l2的长度是小于等于l1的， 所以l2没了的话，不用继续插入
        while l1 and l2  # l2:
            temp = l1.next
            l1.next = l2
            l2 = l2.next
            l1.next.next = temp
            l1 = temp
        return head

    def find_mid(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev