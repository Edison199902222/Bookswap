class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        # 贪心
        # 每次face up 的时候，只想从最小的token 开始
        # 每次face down 的时候，只想翻最大的token
        # 每次尽可能face up token 然后从最大的开始face down 一次
        tokens.sort()
        queue = collections.deque(tokens)
        ans = 0
        cur_score = 0
        while queue and (P >= queue[0] or cur_score > 0):
            while queue and P >= queue[0]:
                P -= queue.popleft()
                cur_score += 1
            ans = max(ans, cur_score)
            if queue and cur_score > 0:
                P += queue.pop()
                cur_score -= 1
        return ans