# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
一道比较经典的题
用 while fast and fast.next: 这个条件 return slow 时 当linklist为偶数时 return的时 第二个中间点
用 while fast.next and fast.next.next: return的是第一个中间点
'''
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow