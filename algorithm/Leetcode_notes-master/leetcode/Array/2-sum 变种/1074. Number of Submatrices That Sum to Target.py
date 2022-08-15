class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        for row in matrix:
            for i in range(n - 1):
                row[i + 1] += row[i] # 把row 的每一个number 都变成是前一个的累计和
        result = 0
        for left in range(n):
            for right in range(left, n):
                dic = collections.defaultdict(int) # 所有小矩形 的累加和
                cur_sum = 0
                dic[0] = 1  # 特殊情况， 如果我们要找的k = 大matrix 的值
                for row in range(m):
                    if left > 0:
                        cur_sum += matrix[row][right] - matrix[row][left - 1] # 如果左边界大于0 的话， 那么我们大矩阵累计和 要减去前面一根的累计和
                    else:
                        cur_sum += matrix[row][right]
                    result += dic[cur_sum - target]  #  cur - target = x 代表 我们当前大矩阵比目标矩阵大多少， 如果大矩阵中存在一个等于x的矩阵的话，cursum - x = target
                    dic[cur_sum] += 1
        return result
'''
思路是， 如果我们现在有一个大矩形累加和， 里面有N 个小矩形的累加和，如果target在里面的话， 那么用大矩形 - target 的值 就是我们要找的小矩形的值
我们先让matrix 的每一个位置， 都是这一行 前面col的累加和 变成一个pre sum
然后 我们遍历 col 把 每一个col 尝试设置成我们的左边界
    把左边界到 col 最大值 尝试设置成我们的右边界
    设置一个dic 记录所有走过小矩形的累加和， 初始化设置0是因为 如果如果我们要找的k = 大matrix 的值， 我们要找的小矩形也就是0
    cur sum 意思是， 每一个我们现在所围成的大矩形的累加和
    所以我们遍历 row， 设置我们的下界， 
    并且如果左边界大于0 那么我们大矩阵累计和 要减去左前面一根的累计和
    不大于0 直接加就行
    然后 我们每一次在dic 中找 有没有存在一个小矩形的累加和 是等于 我们大矩形 - target
    记录每一层大矩形的面积， 因为在下一次中，上一次的大矩形也变成小矩形了， 因为下界一直在增加
'''