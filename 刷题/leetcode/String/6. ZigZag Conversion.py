'''
先创建好zigzag
然后 用row来表示在哪个row要加东西 step表示是+还是-
如果row 是 《 nums的话 继续加1 如果不是 则需要- n
'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # edge case
        if numRows == 1 or numRows > len(s):
            return s
        # 创建 numsrow 这么多行
        string = ["" for i in range(numRows)]
        # 表示当前遍历到哪一个row
        row = 0
        # 当前的方向
        steps = 1
        # 思路：竖着看，每次给第row 行添加上当前字符后，row 加上 steps 也就是方向，如果row 没有到最后一行
        # 那么方向就是正的，不然就是反向
        for i in s:
            string[row] += i
            if row == 0:
                steps = 1
            elif row == numRows - 1:
                steps = - 1
            row += steps
        return "".join(string)
