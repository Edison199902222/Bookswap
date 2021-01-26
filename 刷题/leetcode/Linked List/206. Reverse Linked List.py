# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        cur = head
        pre = None

        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head  # 意思是是 1 ->2 - >3 | 3 是new head，我们递归到2时，把3 指向2 就是 head.next.next = head
        head.next = None
        return new_head


'''
递归 
base case 如果 not head 或者 head 下一个没有的话 我们就返回 head 说明 递归到尾部了
然后 我们递归 head next 直到 递归到倒数第二个节点 因为 最后一个节点的next 是none 我们不需要指针反转 None 不能指向任何东西
递归到倒数第二个node时  我们只需要把 尾部的节点 指向自己 然后再把自己 指向 none 就行了


'''
