# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
用dummy 插入
然后有三个指针 pre m n
pre 是m 前一个指针
先让 pre 跟 m 走到位置
然后让n 也走到 位置
然后每次让m 插入到n的后面 同时 m每次都是pre的下一个
直到m与n重合 就说明reverse 完了
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        # 让prev走到m 前一个
        prev = dummy
        for i in range(m - 1):
            prev = prev.next
        # 创建cur  指向第m个node 开始翻转， 跟翻转链表一样
        reverse = None
        cur = prev.next
        for i in range(n - m + 1):
            temp = cur.next
            cur.next = reverse
            reverse = cur
            cur = temp
        # 翻转后，reverse 是 第n 个node，cur 是n + 1 node
        # 把prev 下一个node 的下一个 设置成n + 1个node 也就是把之前prev 的下一个设置成尾部
        # 把prev 下一个设置成reverse
        prev.next.next = cur
        prev.next = reverse
        return dummy.next
