"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""


class Solution:
    """
    @param A: a list of integer
    @return: The root of Segment Tree
    """

    def build(self, A):
        # write your code here
        return self.build_tree(0, len(A) - 1, A)

    def build_tree(self, start, end, A):
        if start > end:
            return None
        root = SegmentTreeNode(start, end, A[start])
        if start == end:
            return root
        mid = (start + end) // 2
        root.left = self.build_tree(start, mid, A)
        root.right = self.build_tree(mid + 1, end, A)
        if root.left and root.left.max > root.max:
            root.max = root.left.max
        if root.right and root.right.max > root.max:
            root.max = root.right.max
        return root