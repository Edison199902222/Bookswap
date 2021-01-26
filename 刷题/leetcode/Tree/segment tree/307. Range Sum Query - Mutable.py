class Segment_node(object):
    def __init__(self, start, end, sums):
        self.start = start
        self.end = end
        self.sums = sums
        self.left = None
        self.right = None


class Segment_tree(object):
    def __init__(self, A):
        self.root = self.build(0, len(A) - 1, A)

    # 建立树
    def build(self, start, end, A):
        if start > end:
            return
            # 一开始要把sums 设置成0， 不然会反复添加
        root = Segment_node(start, end, 0)
        if start == end:
            return Segment_node(start, end, A[start])
        root.left = self.build(start, (start + end) // 2, A)
        root.right = self.build((start + end) // 2 + 1, end, A)
        # 建立完左 右， 需要更新当前sums
        if root.left:
            root.sums += root.left.sums
        if root.right:
            root.sums += root.right.sums
        return root

    # 更新某一个index的value
    def modify(self, root, index, value):
        if not root:
            return
        if root.start == root.end:
            root.sums = value
            return
        if root.left.end >= index:
            self.modify(root.left, index, value)
            root.sums = root.left.sums + root.right.sums
        else:
            self.modify(root.right, index, value)
            root.sums = root.left.sums + root.right.sums

    # 得到start 到 end 这一段的sums
    def query(self, start, end, root):
        if start > root.end or end < root.start:
            return 0
        if start <= root.start and root.end <= end:
            return root.sums
        left = self.query(start, end, root.left)
        right = self.query(start, end, root.right)
        print(left, right)
        return left + right


class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = Segment_tree(nums)

    def update(self, i: int, val: int) -> None:
        node = self.tree
        node.modify(node.root, i, val)

    def sumRange(self, i: int, j: int) -> int:
        node = self.tree
        return node.query(i, j, node.root)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)