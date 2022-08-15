class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.result = []
        n = len(characters)
        k = combinationLength
        # generate bitmasks from 000 to 111
        # 111 代表全部都选
        # 因为是从小到大的值， 所以result 的逆序的
        for bitmask in range(1 << n):
            # 数当前bit 有几个1
            # 如果跟我们需要的1 相等
            if bin(bitmask).count("1") == k:
                cur = []
                # 那就遍历当前bit，检查哪一位是1，添加对应的char 进result
                # 先检查char 的0 号位， 但在bit中 0 号位是最高位，所以用n - j - 1 用1 来检查
                for j in range(n):
                    if bitmask & (1 << n - j - 1):
                        cur.append(characters[j])
                self.result.append("".join(cur))

    def next(self):
        """
        :rtype: str
        """
        return self.result.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.result) > 0

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()