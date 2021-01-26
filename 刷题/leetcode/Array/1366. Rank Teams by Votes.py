class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        # 通过题目， 排名是根据每个位置投票的结果，投票最多的那个被安排在当前位置，如果都一样，那么看的是下一个， 如果全一样，看的是字母顺序
        # 所以，想到 每个字母 对应一个列表，列表上储存的是每个位置的投票结果，最后还要加上一个当前字母 这样可以break tie 然后根据这个 去排序
        n = len(votes[0])
        vote_count = {x: [0 for i in range(n)] + [x] for x in votes[0]}
        for vote in votes:
            for i, x in enumerate(vote):
                # 给投票的位置减1， 因为sort 是从小到大排序，越小的其实 票数越高
                vote_count[x][i] -= 1
        # 根据整个列表排序
        ans = sorted(list(votes[0]), key=lambda x: vote_count[x])

        return ''.join(ans)