# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
用merge sort去做
先把list 拆成一个一个
然后每次调用merge 去合并
最后返回
So it iterates over the linked lists lg(N) times, making the time complexity O(M*lg(N)), where M is the size of the merged linked list and N is the size of the lists argument.
Space complexity with recursion stack is O(lg(N)), without recursion stack is O(1)
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists) <= 1:
            return lists[0]
        return self.merge_list(lists, 0, len(lists) - 1)

    def merge_list(self, lists, start, end):
        if start == end:
            return lists[start]
        mid = (start + end) // 2
        left = self.merge_list(lists, start, mid)
        right = self.merge_list(lists, mid + 1, end)
        return self.merge(left, right)

    def merge(self, head1, head2):
        dummy = cur = ListNode(0)

        while head1 and head2:
            if head1.val <= head2.val:
                cur.next = head1
                cur = cur.next
                head1 = head1.next
            else:
                cur.next = head2
                cur = cur.next
                head2 = head2.next
        if head1:
            cur.next = head1
        if head2:
            cur.next = head2
        return dummy.next



