class Solution(object):
    def closestToTarget(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        cur = set()
        result = float("inf")
        for num in arr:
            temp = set()
            for j in cur:
                temp.add(j & num)
            cur = temp
            cur |= {num}
            for j in cur:
                result = min(result, abs(j - target))
        return result