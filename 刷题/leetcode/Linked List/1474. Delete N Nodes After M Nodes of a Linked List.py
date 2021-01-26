# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteNodes(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        # 第一步，设置dummy，连接头
        # 第二步 设置count， 算m， 每次 让cur  走到要断开的node 的前一个
        # 第三步， 断开 n 个node，把count 初始化
        # 第四步，cur 继续走
        dummy = cur = ListNode(0)
        dummy.next = head
        count = 0
        while cur:
            if count < m:
                count += 1
            else:
                j = 0
                while j < n and cur.next:
                    j += 1
                    cur.next = cur.next.next
                count = 1
            cur = cur.next
        return dummy.next
