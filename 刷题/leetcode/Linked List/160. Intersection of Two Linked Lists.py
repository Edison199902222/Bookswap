# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
两个链表 两个指针 p1 p2
都是从头开始走 如果任何一个指针 指到None
然后就从另一个链表的开头走 直到相遇就return
原理就是 如果两个链表 合起来
两个指针 其实走的路是一样多的 因为走到空 就换一个链表走

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1 = headA
        l2 = headB
        # 想成分开的两幅图， head a 的尾部与 headb的头部连起来了
        # head b 的 尾部 跟head a 的头部连起来了
        # 两个 指针 走的路程是相等的， 只是谁先走而已，把 intersection point 看成终点
        # 两个指针 到达终点的时间是一样的， 所以相遇的时候就是intersection
        while l1 != l2:
            if not l1:
                l1 = headB
            else:
                l1 = l1.next
            if not l2:
                l2 = headA
            else:
                l2 = l2.next
        return l1
