# Definition for singly-linked list.
'''
需要先建立一个node 连接在head 之前 这是防止特殊情况 【1】 1 None type have no next
然后需要每次检查 cur 的next 是不是空 不是空的话 我们再检查下一个node 的val 跟我们目标值是不是相等
如果相等的话 那么我们把cur node 的next 直接设置成下下个node 此时 千万不要更新cur
因为链表发生了变动 我们不知道 下下个node 的下一个是不是none 
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None: return head
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy
        while current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next
if __name__=='__main__':
    solution=Solution()
    p1=ListNode(1)
    print(solution.removeElements(p1,1))