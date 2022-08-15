class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefix = []
        prefix = 0
        for i in range(len(w)):
            prefix += w[i]
            self.prefix.append(prefix)
        self.total = prefix

    def pickIndex(self):
        """
        :rtype: int
        """
        target = self.total * random.random()
        left = 0
        right = len(self.prefix)
        while left + 1 < right:
            mid = (left + right)//2
            if self.prefix[mid] >= target:
                right = mid
            else:
                left = mid
        if self.prefix[left] > target:
            return left
        else:
            return right
'''
算出每个index 对应的累计和
然后用total sum 乘 random
然后看 这个target 落在哪个范围里
'''

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()