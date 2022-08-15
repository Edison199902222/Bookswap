# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        prefix = 0
        seen = {}
        # 把前缀和0放进去，有可能整个linked list 等于 0
        seen[0] = dummy = ListNode(0)
        dummy.next = head
        # 把前缀和 放进seen 中
        while head:
            prefix += head.val
            seen[prefix] = head
            head = head.next

        head = dummy
        prefix = 0
        # 如果 后面存在相同的前缀和的话， 说明 当前node  到 下一个相同前缀和的node 这一段的val 是0， 因为对总前缀和没有任何的增加
        while head:
            prefix += head.val
            head.next = seen[prefix].next
            head = head.next
        return dummy.next