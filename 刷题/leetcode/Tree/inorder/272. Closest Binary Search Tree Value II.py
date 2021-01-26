# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        large_stack = []
        small_stack = []
        # 把最靠近target的node 分成两类，放进两个stack中
        # 一个大于target， 一个小于等于 target
        while root:
            if root.val <= target:
                small_stack.append(root)
                root = root.right
            else:
                large_stack.append(root)
                root = root.left
        result = []
        # for循环k次，每次比较prev_stack和next_stack栈顶节点的值，把与target距离近的那个放进results中。
        for i in range(k):
            # 如果large stack 中的top node没了，那么需要另一个node补上。
            # For large_stack refill, we want the new added nodes as small as possible but still larger than target.
            if large_stack and (
                    len(small_stack) == 0 or abs(large_stack[-1].val - target) <= abs(small_stack[-1].val - target)):
                result.append(large_stack[-1].val)
                self.get_next(large_stack, large_stack.pop())
            # For small_stack refill, we want the new added nodes as large as possible but still smaller than target.
            elif small_stack:
                result.append(small_stack[-1].val)
                self.get_prev(small_stack, small_stack.pop())
        return result

    def get_next(self, stack, root):
        root = root.right
        while root:
            stack.append(root)
            root = root.left

    def get_prev(self, stack, root):
        root = root.left
        while root:
            stack.append(root)
            root = root.right

'''
暴力 on
如果此时结果数组不到k个，直接将此节点值加入结果 res 中，
如果该节点值和目标值的差值的绝对值小于结果 res 的首元素和目标值差值的绝对值，
说明当前值更靠近目标值，则将首元素删除，末尾加上当前节点值，
反之的话说明当前值比结果 res 中所有的值都更偏离目标值，由于中序遍历的特性，之后的值会更加的遍历，所以此时直接返回最终结果即可
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        self.queue = collections.deque()
        self.helper(root, target, k)
        return self.queue

    def helper(self, root, target, k):
        if root is None:
            return
        self.helper(root.left, target, k)
        if len(self.queue) < k:
            self.queue.append(root.val)
        elif abs(root.val - target) < abs(self.queue[0] - target):
            self.queue.popleft()
            self.queue.append(root.val)
        else:
            return
        self.helper(root.right, target, k)

