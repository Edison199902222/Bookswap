# Definition for singly-linked list.
'''
用pre cur cur.next三个指针
每次检查 cur next 指针 跟cur的关系
如果大于 现在的node  那么跳过 因为已经排序好了
如果小于 那么我们就需要再检查
检查cur next 是不是小于pre next
如果还小于的话 那么我们pre就需要等于dummy 然后从头遍历 因为 如果小于的话 说明cur next这个node 需要插入 比prev 指针指向的node 之前的点
那么我们就 pre = dummy 从头找所需要的位置
然后我们跟 pre next进行比较
直到找到一个 next 大于我们的 cur next val
这说明 我们可以插入了
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = dummy = ListNode(0)
        cur = dummy.next = head
        while cur and cur.next:
            val = cur.next.val
            if val > cur.val:
                cur = cur.next
                continue
            if val < prev.next.val:
                prev = dummy
            while val > prev.next.val:
                prev = prev.next
            new = cur.next
            cur.next = new.next
            new.next = prev.next
            prev.next = new
        return dummy.next
if __name__=='__main__':
    solution=Solution()
    p1=ListNode(-1)
    p2=ListNode(5)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p5 = ListNode(0)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    print(solution.insertionSortList(p1))
