# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
把一个list分成两个list
一个odd list 一个even list
最后把odd list 指向 even list
其实就是 我们每一次 让 odd even 指向它们各自的两个node
因为 even 总是在odd的下一个， 所以 我们如果要判断下面还有node 需要进行操作的话，至少要有两个node，也就是 even 跟 even的下一个，才需要操作

'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 第一步 把原linked list 拆成两部分，一部分odd，一部分even
        # 第二步 在确定evern 跟 even 的下一个还有的情况下， 做拆分， 因为如果even 的下一个没有了，也就是下一个odd 没有了，就没有必要继续走下去
        # 第三步， 每次 先设置odd， 然后设置even
        if not head:
            return None
        odd_node = head
        even_head = head.next
        even_node = head.next
        while even_node and even_node.next:
            # 先把 odd的下一个设置
            odd_node.next = even_node.next
            # odd 往下走一步
            odd_node = odd_node.next
            # 把even 的下一个找到
            next_even = odd_node.next
            # 设置even
            even_node.next = next_even
            # even 走一步
            even_node = even_node.next

        odd_node.next = even_head
        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        odd_node = new_head = ListNode(0)
        even_node = new_head2 = ListNode(0)
        while cur and cur.next:
            odd_node.next = cur.next
            even_node.next = cur.next.next
            odd_node = odd_node.next
            even_node = even_node.next
            # 不能用 cur.next.next 因为 前面even 和 node 的操作 会是的 cur 的下一个发生变化
            cur = even_node
        odd_node.next = new_head2.next
        return new_head.next

