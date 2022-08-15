
'''
其实这个问题是从数学性质角度写的代码，
就好像我不用算就知道42的阶乘结果后有几个0：
因为直接阶乘到42，5 的倍数有5，10，15，20，25，30，35，40，这种情况根本不用担心2的问题，就好像15前一定有2的倍数，
例如12，35前一定有32这样2的倍数。所以最后结尾的0的个数，只需要找到5的个数，一定能找到与它配对相乘等于10的2因数。
所以42的阶乘结尾0的个数就是9个：7个5的倍数：5，10，15，20，30，35，40，由于25特殊一点是5*5，所以算两个，这样加起来一共9个。


'''
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n != 0:
            result += n//5
            n = n//5
        return result
if __name__ == "__main__":
    solution = Solution()
    print(solution.trailingZeroes(5))