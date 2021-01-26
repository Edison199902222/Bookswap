"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of segment tree.
    @param index: index.
    @param value: value
    @return: nothing
    """
    def modify(self, root, index, value):
        # write your code here
        if not root:
            return
        if root.start == root.end:
            root.max = value
            return
        # 如果index 小于等于左边node的end，说明index在左边
        if root.left.end >= index:
            self.modify(root.left, index, value)
        else:
            self.modify(root.right, index, value)
        # 回溯更新max
        root.max = max(root.left.max, root.right.max)