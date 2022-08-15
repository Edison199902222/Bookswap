# Definition for singly-linked list.
'''
两个指针 fast and slow
让fast先走k%length 步
然后 我们需要同时走
让fast 指向链表尾部 slow也会走
停止时 slow 就是新的队尾 会指向None slow的下一个就是new head fast 的下一个会指向头
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 看成把最后k个节点平移到前面
        # 那么需要得到 倒数第k 个节点前一个节点才能操作整个最后k个节点
        if head is None:
            return head
        new_head = head
        length = 0
        # 求出整个list 的长度
        while new_head is not None:
            length += 1
            new_head = new_head.next

        k %= length
        fast = head
        # 先让fast指针走k步
        while k > 0:
            fast = fast.next
            k -= 1
        # 创建slow 指针， 跟fast 指针距离为k
        slow = head
        # 当fast走到list尾部时，slow 距离 fast 还是k，就得到头节点的前一个点 也就是倒数k + 1
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        # 先让最后一个node 指向head
        # 因为一旦 slow 跟head 指向的是同一个,不先设置fast 的下一个的话，头就变成none了
        fast.next = head
        head = slow.next
        slow.next = None
        return head


if __name__=='__main__':
    solution=Solution()
    p1=ListNode(1)
    print(solution.rotateRight(p1,0))