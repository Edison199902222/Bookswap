# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
用slow fast 去弄到链表中间位置
slow每次走一步 fast每次走两步
'''
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None
        return self.helper(head,None)


    def helper(self,start,end):
        if start == end:return None
        slow,fast = start,start
        while fast != end and fast.next != end:
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        root.left = self.helper(start,slow)
        root.right = self.helper(slow.next,end)
        return root


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # time : on, space : logn
        # 中序遍历
        # 对于bst 来说，中序遍历 是 按照数从小到大的顺序的
        # 所以先到left 最底下，然后先构造最左边node，这就是链表第一个node
        # 然后再构造当前node， 然后再构造右边的node
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        self.node = head
        return self.helper(0, length - 1)

    def helper(self, start, end):
        if start > end:
            return None
        mid = (start + end + 1) // 2
        left = self.helper(start, mid - 1)
        root = TreeNode(self.node.val)
        self.node = self.node.next
        root.left = left
        right = self.helper(mid + 1, end)
        root.right = right
        return root

