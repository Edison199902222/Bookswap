# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        # 同一个垂直度的node 储存在同一个list
        dic = collections.defaultdict(list)
        # 创建queue， 层序遍历，里面储存root 和 level值
        queue = collections.deque([(root, 0)])
        # 从上往下遍历树，把level 跟 node 放进字典里，然后把左右子树放进queue中 继续遍历
        while queue:
            node, level = queue.popleft()
            dic[level].append(node.val)
            if node.left:
                queue.append((node.left, level - 1))
            if node.right:
                queue.append((node.right, level + 1))
        result = []
        # 最后一步，排好序 放进result中
        candidate  = sorted(dic.keys())
        for key in candidate:
            result.append(dic[key])
        return result