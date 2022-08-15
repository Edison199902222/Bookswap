
'''
想象成链表
每一次 处理下一层， 把下一层连起来
'''

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # 头节点， 每一层的头节点
        head = root
        while head:
            # 当前层头节点
            cur = head
            # 初始化 下一层的前置节点与 头节点
            prev = head = None
            while cur:
                if cur.left:
                    # prev 是 none  说明下一层前置节点 跟 头节点还没找到
                    if prev is None:
                        head = prev = cur.left
                    # 不是none，说明下一层的已经找到前置节点，跟头节点，更新前置节点就行
                    else:
                        prev.next = cur.left
                        prev = prev.next
                if cur.right:
                    if prev is None:
                        head = prev = cur.right
                    else:
                        prev.next = cur.right
                        prev = prev.next
                cur = cur.next
        return root



'''
每层处理当前层
'''

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return
        queue = collections.deque([root])
        while queue:
            # 得到当前层有多少node
            size = len(queue)
            for i in range(size):
                # 在这一层 把每个node pop出来
                node = queue.popleft()
                # 小于 size - 1 意思是只要还有一个node， 就把当前node 的next 指向下一个
                if i < size - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
