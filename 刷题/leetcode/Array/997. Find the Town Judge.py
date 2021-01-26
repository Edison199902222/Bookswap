class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trust_score = [0] * (N + 1)
        for person_1, person_2 in trust:
            trust_score[person_1] -= 1
            trust_score[person_2] += 1
        for i in range(1, N + 1):
            if trust_score[i] == N - 1:
                return i
        return - 1
'''
用图的方式
创建一个trust score 表示 每个的人的分数 如果有一个人的分数 会等于所有人的数量 - 1 那么这人就是答案
并且 trust score 表示从index 1 到 index n + 1 这样是为了 防止index溢出
然后遍历trust person1 依赖 person2 那么我们就把person1 减1 分 peroson2 + 1 分
最后检查 谁的分数是 n - 1
'''