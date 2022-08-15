class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        while len(stones) > 1:
            stones.sort()
            stone1 = stones.pop()
            stone2 = stones.pop()
            new_stone = stone1 - stone2
            if new_stone == 0:
                continue
            stones.append(new_stone)
        return stones[0] if len(stones) > 0 else 0
'''
就是排序加模拟
time  nlogn
'''