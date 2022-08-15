class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1,max2,max3,min1,min2 = float('-Inf'),float('-Inf'),float('-Inf'),float('Inf'),float('Inf')
        for num in nums:
            if num > max1:
                max1,max2,max3 = num,max1,max2
            elif num > max2:
                 max3,max2 = max2,num
            elif num > max3:
                max3 = num
            if num < min1:
                min1,min2 = num,min1
            elif num < min2:
                min2 = num
        return max(max1*max2*max3,min1*min2*max1)
if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumProduct([1,2,3]))
'''
因为array 有可能有负数 
所以 我们需要三个 记录 最大三个数的值
两个 最小三个数的值
然后 三个最大数相乘 跟 最小两个数乘最大数的结果比较
'''