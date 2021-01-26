# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        length = 0
        cur = root
        # 先计算长度
        while cur:
            cur = cur.next
            length += 1
        # 算每个区间要放几个element
        chunk_length = length // k
        # 算 整除k之后，还剩下几个
        length_over = length % k

        result = []
        dummy = prev = ListNode(0)
        dummy.next = root
        cur = root
        # 分配k次
        for i in range(k):
            if cur:
                result.append(cur)
                # 还有剩下的话，分配给当前区间多一个， 这样区间的difference 不会超过1
                if length_over > 0:
                    element_length = chunk_length + 1
                else:
                    element_length = chunk_length
                length_over -= 1
                for j in range(element_length):
                    # 细节， 因为prev 下一个设置成了none， 所以无法get 到下一个， 需要等于cur
                    prev = cur
                    cur = cur.next
                # prev指向分配到当前区间的最后一个node， 断开和后面的连接， cur是下一个区间的开始
                prev.next = None
            else:
                result.append(None)
        return result
