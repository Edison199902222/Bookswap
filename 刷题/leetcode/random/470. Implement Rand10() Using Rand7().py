# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        # 想从 rand 7 构造 rand 10
        # 范围在1～7的随机数产生器，即1~7各个数字出现的概率皆为1/7.
        # 范围在1～10的随机数产生器，即1~10各个数字出现的概率皆为1/10.
        # 这个题的构造思路是先构造一个randN，这个N必须是10的整数倍，然后randN % 10就可以得到了rand10.
        # rand7()等概率地产生1,2,3,4,5,6,7.
        # rand7() - 1等概率地产生[0,6].
        # (rand7() - 1) *7等概率地产生0, 7, 14, 21, 28, 35, 42
        # (rand7() - 1) * 7 + (rand7() - 1)等概率地产生[0, 48]这49个数字
        # 如果步骤4的结果大于等于40，那么就重复步骤4，直到产生的数小于40
        # 把步骤5的结果mod 10 再加1， 就会等概率的随机生成[1, 10]

        # N 是已有的，M是想要构造的
        # in this case， 7 * 7 - （7 * 7） % 10
        cur = 40  # 公式是， N * N - (N * N) % M
        while cur >= 40:
            # curr = (randN() - 1) * N + randN() - 1
            cur = (rand7() - 1) * 7 + (rand7() - 1)
        # cur % M + 1
        return (cur % 10) + 1
