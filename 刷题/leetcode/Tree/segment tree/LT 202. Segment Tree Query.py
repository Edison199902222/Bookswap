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
    @param start: start value.
    @param end: end value.
    @return: The maximum number in the interval [start, end]
    """
    def query(self, root, start, end):
        # write your code here
        # 不符合的区间直接return最小值，不用继续往下查找
        if start > root.end or end < root.start:
            return float("-inf")
        # 如果目标区间 被当前区间包括在内，直接return 当前区间max
        # 因为这里面的最大值有可能是目前区间的最大值
        if start <= root.start and root.end <= end:
            return root.max
        return max(self.query(root.left, start, end), self.query(root.right, start, end))