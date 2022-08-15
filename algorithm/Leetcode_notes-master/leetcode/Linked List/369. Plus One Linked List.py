# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 第一步 创建dummy 连接 head，防止999 的情况，dummy 可以变成1
        # 第二步 找到最右边不为9的node
        # 第三步，把最右边不为9 的node 加上1之后， 后面所有的node全部变成0
        # 第四步 判断返回， 如果dummy没有改变的话，返回dummy next， 如果dummy 被改变的话，说明 dummy 之后的node val 全是9， 所以返回dummy
        dummy = ListNode(0)
        dummy.next = head
        not_nine = dummy
        while head:
            if head.val != 9:
                not_nine = head
            head = head.next

        not_nine.val += 1
        not_nine = not_nine.next
        while not_nine:
            not_nine.val = 0
            not_nine = not_nine.next
        return dummy.next if dummy.val == 0 else dummy