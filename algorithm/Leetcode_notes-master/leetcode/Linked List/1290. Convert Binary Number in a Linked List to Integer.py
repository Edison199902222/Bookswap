# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        cur = head
        result = 0
        # 每走一步  2乘之前result 等于 走了多少步，就乘了多少次2
        while cur:
            result = 2 * result + cur.val
            cur = cur.next
        return result
