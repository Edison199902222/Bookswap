class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # 得到有几位是不同的
        # 异或操作 相同位为0， 不同为1
        temp = x ^ y
        count = 0
        while temp != 0:
            # 把最右边的1 去掉
            # 因为 temp - 1 会让temp 最右边的1 拆分掉
            # 然后跟原本temp 取 &，temp - 1 因为原来最右边的1变成0 了
            # and 之后，肯定是0
            temp &= temp - 1
            count += 1
        return count
