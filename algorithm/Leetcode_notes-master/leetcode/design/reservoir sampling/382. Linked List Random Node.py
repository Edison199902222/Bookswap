# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        # reservoir sampling
        count = 0
        cur = self.head
        temp = None
        while cur:
            # 每次抽一个，等概率
            if random.randint(0, count) == count:
                temp = cur
            count += 1
            cur = cur.next
        return temp.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()