# Definition for singly-linked list.
'''
要分成两个函数
主函数 先找到中间节点 然后分成两个list
然后递归拆开 用merge合并
merge 就是用来合并两个链表
最后return head就行
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 第一步， 找到链表中间数， 把链表拆成两半
    # 第二步， 递归到底部，直到 每个链表只含有一个数时，进行merge
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        return self.merge_list(head)

    def merge_list(self, head):
        if not head.next:
            return head
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        second = mid.next
        mid.next = None
        left = self.merge_list(head)
        right = self.merge_list(second)
        return self.merge(left, right)

    def merge(self, head1, head2):
        dummy = cur = ListNode(0)
        while head1 and head2:
            if head1.val <= head2.val:
                cur.next = head1
                head1 = head1.next
                cur = cur.next
                cur.next = None
            else:
                cur.next = head2
                head2 = head2.next
                cur = cur.next
                cur.next = None
        if head1:
            cur.next = head1
        if head2:
            cur.next = head2
        return dummy.next


if __name__=='__main__':
    solution=Solution()
    p1=ListNode(4)
    p2=ListNode(2)
    p3 = ListNode(1)
    p4 = ListNode(3)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    print(solution.sortList(p1))