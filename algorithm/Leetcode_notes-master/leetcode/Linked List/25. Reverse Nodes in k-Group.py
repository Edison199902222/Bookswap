# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
分为两个函数
第一个函数： 只反转链表
第二个函数： 找到需要反转的链表后 使用第一个函数 去反转
每一轮循环 我们可以看作 pre -> start -> ..... -> end -> next
我们每次反转 start 到 end 这一段
pre end -> ... -> start next 然后连接 pre 跟next
pre -> end -> ... -> start -> next
然后继续寻找下一轮反转的
'''
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        pre = dummy
        pre.next = head
        start = head
        end = head
        count = 1
        while start and end:
            if count < k:
                count += 1
                end = end.next
            else:
                count = 1
                new_start = end.next
                self.reverse(start, new_start) # 为什么我们放进去的是new_start而不是end呢？ 因为使用反转函数时， 我们需要遇到end后面一个 也就是new_start时 需要停止
                pre.next = end
                start.next = new_start
                pre = start
                end = new_start
                start = new_start
        return dummy.next

    def reverse(self, start, end):
        pre = None
        cur = start
        while cur != end: # 普通反转链表只需要判断cur不等于none但是 我们cur 下一个有可能不是none， 也就是 end 下一个有可能不是none，
            # 所以我们的end需要的是需要反转的链表的结尾的下一个节点， 用它来判断
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

    '''
    如果不足k个 也要翻转的情况
    '''

    class Solution:
        def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
            dummy = prev = ListNode(0)
            dummy.next = head
            start = end = prev.next
            count = 1
            while start and end.next:
                if count < k:
                    count += 1
                    end = end.next
                else:
                    count = 1
                    # start 到 end 要翻转， end下一个不需要翻转，就是我们新的需要遍历的头
                    new_start = end.next
                    self.reverse(start, new_start)  # 翻转start 到 end， new start用来判断什么时候终止
                    prev.next = end
                    start.next = new_start
                    # 变成 翻转头的前一个
                    prev = start
                    start = new_start
                    end = new_start
            self.reverse(start, end.next)
            prev.next = end
            return dummy.next

        def reverse(self, start, end):
            prev = None
            while start != end:
                temp = start.next
                start.next = prev
                prev = start
                start = temp



