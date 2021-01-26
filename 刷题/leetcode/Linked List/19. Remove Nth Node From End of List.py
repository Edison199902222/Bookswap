# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
这道题跟链表中倒数第k个节点 有点像 但不全是
首先要在链表首 插入一个dummy
然后 建立两个指针 指向dummy
fast 指针先移动n次
然后两个指针同时移动
这样slow指针就是我们要移除指针的前一个
再把slow的next设置为next next就好
'''


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return head
        # 创建dummy 防止 [1] 1的情况，把list里面全部都移除
        dummy = ListNode(0)
        dummy.next = head
        # 创建fast 指针，先走n步
        fast = dummy
        while n > 0:
            fast = fast.next
            n -= 1
        # 创建slow指针， 保证与 fast 距离是k
        slow = dummy
        # 走到倒数第n个node 的前一个node 因为fast走到最后是 最后一个node， 跟slow 距离为n
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        temp = slow.next.next
        slow.next = temp
        return dummy.next