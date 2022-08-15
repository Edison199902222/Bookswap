class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        cur = arr[0]
        win = 0
        # 遍历列表，如果发现后面的数比cur小，win 的次数就 + 1
        # 如果大的话，cur 就更新，win也更新
        # win 如果等于 k，直接return当前cur
        # 数组结束发现还没有等于k的，直接return cur， 因为cur 是此时数组最大值
        for i in range(1, len(arr)):
            if arr[i] > cur:
                cur = arr[i]
                win = 0
            win += 1
            if win == k:
                return cur
        return cur