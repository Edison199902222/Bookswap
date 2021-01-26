class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        # 追踪 需要的moves 用了几次
        dic = collections.defaultdict(int)

        for i in range(len(s)):
            if s[i] == t[i]:
                continue
            # 如果小于的话, a，b 直接就可以转
            if ord(s[i]) < ord(t[i]):
                move = ord(t[i]) - ord(s[i])
            # b a 这种不可以直接算，用 a - b + 26
            else:
                move = ord(t[i]) - ord(s[i]) + 26
            # 从dic 中找到最少需要的move， 然后乘上它之前用了几次，
            if dic[move] * 26 + move > k:
                return False
            dic[move] += 1
        return True