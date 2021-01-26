# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
用一个快慢指针 加上rev指针去写
快 指针每次移动 两格 慢指针每次移动一个 同时 把rev 每一次都逆向指向自己 并且更新为slow
比如 1 -> 2 -> 3  rev第一次等于1 然后指向之前的自己 就是 1 -> None, 2 -> 1 -> None
要注意 如果链表是奇数的时候， slow 还需要移动一次才可以指向我们要比较的第一个node
最后 比较rev 与 slow相等不相等就行
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        dummy = None
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            temp1 = slow.next
            temp2 = dummy
            dummy = slow
            dummy.next = temp2
            slow = temp1
        # 如果链表为偶数个数， fast会为none
        # 如果链表 为奇数个数 fast 会指向最后一个node
        # 我们想要slow 指向的是中间位置的 后面一个
        # 所以为奇数时，slow 需要再走一个
        if fast:
            slow = slow.next
        while dummy:
            if dummy.val != slow.val:
                return False
            dummy, slow = dummy.next, slow.next
        return True
