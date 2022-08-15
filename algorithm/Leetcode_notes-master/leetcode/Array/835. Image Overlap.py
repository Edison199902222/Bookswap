class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        A_list = []
        B_list = []
        # 找到所有为1的点
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    A_list.append((i, j))
                if B[i][j] == 1:
                    B_list.append((i, j))

        dic = collections.defaultdict(int)
        result = 0
        # 遍历两个矩阵为1的点，计算他们的差，含义是 知道要经过几个操作才可以从a 到 b
        # 然后把结果放进dic中，最终相同操作最多的， 就是要寻找的操作
        for i in A_list:
            for j in B_list:
                temp = (i[0] - j[0], i[1] - j[1])
                dic[temp] += 1
                result = max(result, dic[temp])
        return result