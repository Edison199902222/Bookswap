# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
因为这道题 分为偶数情况跟奇数的情况
所以我们需要用三个index pre prenext prenextnext去弄
每次 让pre的next指向prenextnext
prenextnext指向prenext
prenext指向 pre nxtnextnext 这样就完成了交换
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        prev = dummy
        prev.next = head
        while prev.next and prev.next.next:
            temp = prev.next
            temp2 = prev.next.next
            temp3 = temp2.next
            prev.next = temp2
            temp2.next = temp
            temp.next = temp3
            prev = temp
        return dummy.next
'''
创造一个prev node 指向所有node 之前的
保证满足 pre 下一个有node  跟下下一个有node 时 我们进行交换
每次 我们 创建三个temp node
分别是 pre 的下一个  temp1
pre 的下一个的下一个 temp2
pre 的下一个的一下个 的下一个 temp3
pre -> temp1 -> temp2 -> temp3
每一次 我们要实现temp1 跟 temp2 的交换
那么 先把prev 指向 temp2 
然后temp2 指向 temp1 
temp1 指向temp1 
pre -> temp2 -> temp1 -> temp3
再把prev指针指向 temp1 
继续进行下一轮变换

'''



