'''
时间复杂度是o（n）空间复杂度是O(n)
其实空间可以降下来 我们可以用两个数去get就好
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3: return n
        result = [0,1,2,3]
        for i in range(4,n+1):
            result_temp = result[i-1] + result[i-2]
            result.append(result_temp)
        return result[n]

if __name__ == "__main__":
    soluiton = Solution()
    print(soluiton.climbStairs(4))
