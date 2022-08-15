class SnapshotArray:

    def __init__(self, length: int):
        # 初始化，一开始什么都没变的时候，每个值都是0
        self.A = [[[-1, 0]] for i in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        # 每次set，都记录当前index 的变化
        self.A[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # 找到当前index变化中， 利用二分找到，最接近snap_id的这个数，这就是最近变化
        # 因为bisect 只能找第一个大于等于的数， 所以 找比当前snap id 大1的，然后 - 1就行了
        i = bisect.bisect(self.A[index], [snap_id + 1]) - 1
        return self.A[index][i][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)