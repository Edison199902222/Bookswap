class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = [int(x) for x in str(num)]
        max_index = len(num) - 1
        x = y = 0
        # 从右往左遍历， max_index 指向右边最大的数
        #  x 和 y 指向 要交换的两个数
        for i in range(len(num) - 2, - 1, - 1):
            # 如果当前数比最大数大，那就更新
            if num[i] > num[max_index]:
                max_index = i
            # 如果当前数比最大数小，更新 x 和 y， 说明右边的 有数比当前数大
            elif num[i] < num[max_index]:
                x = i
                y = max_index
        num[x], num[y] = num[y], num[x]
        # 不能直接str(num)， [1,2,3] => ['[', '1', ',', ' ', '2', ',', ' ', '3', ']']
        return int("".join([str(x) for x in num]))


