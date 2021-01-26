class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        number = 1
        todo = num
        while todo:
            num = num ^ number
            number = number << 1
            todo = todo >> 1
        return num
'''
num ^ number检查 最低位， 如果最低位是1 那么就会变成0， 如果最低位是1 num那么就会变成0 因为异或是 ab两值相同为0 不同为1 所以我们用number = 1 去测试 如果跟1 相同 那么也是1 就会变成0
每次只弄一位， 所以number 跟todo 都需要动一位数
'''