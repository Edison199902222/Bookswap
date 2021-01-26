class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        # 变成累计和
        for i in range(m):
            for j in range(1, n):
                mat[i][j] += mat[i][j - 1]
        # 总体来说，当L = R 一样时， 会算出对于当前这一行来说 竖着方向上所有可以形成的submatiix/ 横着 长度为1 的所有小矩阵
        # 当 L != R 时， 算出 横着所有长度为 r - l + 1有多少个矩阵 并且看能否和上面拼凑在一起
        result = 0
        for left in range(n):
            for right in range(left, n):
                # 记录 当前上面有几个跟当前size 相等的小矩阵，如果有的话， 每增加一个， 可以多出来 count 这么多个submatrix
                continues_count = 0
                for bottom in range(m):
                    # 求出当前row_sum between left, right
                    if left != 0:
                        cur_sum = mat[bottom][right] - mat[bottom][left - 1]
                    else:
                        cur_sum = mat[bottom][right]
                    #
                    width = right - left + 1
                    if cur_sum == width:
                        continues_count += 1
                    else:
                        continues_count = 0
                    result += continues_count

        return result

