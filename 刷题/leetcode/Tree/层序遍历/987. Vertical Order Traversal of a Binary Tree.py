# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dic = collections.defaultdict(list)
        queue = collections.deque([(root, 0, 0)])
        result = []
        while queue:
            for i in range(len(queue)):
                node, x, y = queue.popleft()
                dic[x].append((y, node.val))
                if node.left:
                    queue.append((node.left, x - 1, y - 1))
                if node.right:
                    queue.append((node.right, x + 1, y - 1))

        temp = sorted(dic.keys())
        for temp_list in temp:
            list1 = sorted(dic[temp_list], key=lambda x: (x[0], -x[1]), reverse=True)
            result.append([list1[i][-1] for i in range(len(list1))])

        return result


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dic = collections.defaultdict(list)
        queue = collections.deque([(root, 0, 0)])
        result = []
        while queue:
            for i in range(len(queue)):
                node, x, y = queue.popleft()
                dic[x].append((y, node.val))
                if node.left:
                    # 其实不用lambda 排序，只需要让y一直加，这样和value 的排序是一样的
                    queue.append((node.left, x - 1, y + 1))
                if node.right:
                    queue.append((node.right, x + 1, y + 1))

        temp = sorted(dic.keys())
        for temp_list in temp:
            list1 = sorted(dic[temp_list])
            result.append([list1[i][-1] for i in range(len(list1))])

        return result