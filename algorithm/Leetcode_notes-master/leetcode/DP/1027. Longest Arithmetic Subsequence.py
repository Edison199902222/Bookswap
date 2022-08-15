class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = {}
        for i in range(len(A)):
            for j in range(i):
                difference = A[i] - A[j]
                if (j, difference) not in dp:
                    dp[(i, difference)] = 2
                else:
                    dp[(i, difference)] = dp[(j, difference)] + 1
        return max(dp.values())