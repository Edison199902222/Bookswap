
'''
在链表前插入dummy 并 current = dummy
然后检查 如果current的下一个 跟下下个相等 那么val = current next 的val 那么就用while循环 把current的指针指向下下个
如果不相等的话 则 = 下一个node
'''

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        # cur指向dummy
        cur = dummy
        # 当cur 还有两个 node 的时候。才可以进行比较
        while cur.next and cur.next.next:
            # 两个相等时，一个一个检查
            if cur.next.val == cur.next.next.val:
                val = cur.next.val
                # 如果cur 下一个 跟 value一样的话，就跳过
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                # 下面两个不一样的话，移动cur
                cur = cur.next
        return dummy.next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        node = head
        prev = None
        while node:
            if node.next:
                if node.val == node.next.val:
                    prev = node.val
                    node = node.next.next
                    continue
            if node.val == prev:
                node = node.next
                continue
            cur.next = node
            cur = cur.next
            node = node.next
            cur.next = None
        return dummy.next