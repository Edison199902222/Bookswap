# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        queue = collections.deque([root])
        result = []
        while queue:
            # 如果当前node是None的话，直接添加#
            node = queue.popleft()
            if node is None:
                result.append("#")
                continue
            # 如果不是None的话， 把node 的value 放进result 中，再把左右孩子放进queue中 继续bfs
            else:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        # 空间优化， 把最后一层的# 全部去掉
        for i in range(len(result) - 1, -1, -1):
            if result[i] == '#':
                result.pop()
            else:
                break
        return ','.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0: return None
        # 把所有node 放进 nodes 列表中
        nodes = collections.deque(data.split(","))
        # 把第一个变成tree node
        root = TreeNode(int(nodes.popleft()))
        # 把第一个root 放进queue 中
        queue = collections.deque([root])
        while queue:
            cur = queue.popleft()
            # 每一次必须要检查， nodes列表中是否还有node， 没有node 说明需要return了
            if len(nodes) == 0:
                break
            left = nodes.popleft()
            # 需要检查 子节点是不是有效的，如果遇到# 就跳过
            if left != "#":
                cur.left = TreeNode(int(left))
                queue.append(cur.left)
            # 对右边进行同样操作
            if len(nodes) == 0:
                break
            right = nodes.popleft()
            if right != "#":
                cur.right = TreeNode(int(right))
                queue.append(cur.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """

        def dfs(root):
            if not root:
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        res = []
        dfs(root)
        return ",".join(res)
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        nodes = data.split(",")
        head = None
        # 储存之前的节点
        stack = []
        for i in nodes:
            node = int(i)
            # 设置root
            if not head:
                head = TreeNode(node)
                stack.append(head)
            else:
                temp = TreeNode(node)
                # 如果当前node 值小于 最近一个的node
                if node < stack[-1].val:
                    stack[-1].left = temp
                # 如果不小于 只能往上找
                else:
                    while stack and node > stack[-1].val:
                        root = stack.pop()
                    root.right = temp
                stack.append(temp)
        return head
    '''
    因为是先序遍历，所以一旦遍历完左节点，左节点就可以丢掉了
    后面不会出现比左节点小的值了
    建立树 是先建立左边，然后右边找地方插
    '''