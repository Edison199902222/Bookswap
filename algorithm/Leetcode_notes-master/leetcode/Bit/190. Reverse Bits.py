'''
& 意思是 如果位数同时为1 则为1
不然贼为0
&1 意思是 检查最后一位是不是等于1 不是就是0
'''


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # 每次往左移动一次result，然后把 temp 合并
            temp = 1 & n
            result = result << 1
            result = result | temp
            # 合并完成后，往右移动1位
            n = n >> 1
        return result

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            # 先检查当前位是不是1
            temp = (n >> i) & 1
            # 先把result往左移动一次
            result = result << 1
            # 然后看当前位是不是1
            result = result | temp
        return result