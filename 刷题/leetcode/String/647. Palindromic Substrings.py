class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        count = 0
        for i in range(len(s)):
            count += self.extend(s, i, i)
            count += self.extend(s, i, i + 1)
        return count

    def extend(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    print(solution.countSubstrings("aaa"))
