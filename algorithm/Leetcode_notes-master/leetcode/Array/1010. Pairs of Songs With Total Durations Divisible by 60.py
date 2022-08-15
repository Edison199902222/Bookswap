class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        dic = [0] * 60
        sums = 0
        for cur in time:
            sums += dic[(60 - cur % 60) %60]
            dic[cur % 60] += 1
        return sums
'''
用一个长度为60 的数组 记录除以60 余数相同歌曲的数量
比如dic[i]表示除以60 余数为i的歌曲数量
用sums 记录 满足条件的pairs
遍历time 
每遇到一首歌cur 
我们就先查找是不是有另一个数 跟我们的和可以组成满足条件的
所以 cur % 60 是先求余数 然后用 60 - 余数 就可以得到我们想要的目标数 但是 万一cur 是 60的话 最后结果也是60，
但是我们希望 最后结果是0 因为数组中只有0 ～ 59， 所以我们再做一次 % 60 防止越界
然后更新余数

'''