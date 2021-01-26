# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val >= l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next

        while l1:
            cur.next = l1
            cur = cur.next
            l1 = l1.next

        while l2:
            cur.next = l2
            cur = cur.next
            l2 = l2.next
        return dummy.next


if __name__=='__main__':
    solution=Solution()
    p1=ListNode(1)
    p2=ListNode(2)
    p3=ListNode(3)
    p1.next=p2
    p2.next=p3
    p4 = ListNode(1)
    p5 = ListNode(2)
    p6 = ListNode(3)
    p1.next = p2
    p2.next = p3
    p4.next = p5
    p5.next = p6
    print(solution.mergeTwoLists(p1,p4))