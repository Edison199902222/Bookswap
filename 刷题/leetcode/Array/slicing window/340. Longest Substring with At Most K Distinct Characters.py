class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0
        counter = collections.Counter()
        count = 0
        result = 0
        left = 0
        for right in range(len(s)):
            counter[s[right]] += 1
            if counter[s[right]] == 1:
                count += 1
            while count > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    count -= 1
                left += 1
            result = max(result, right - left + 1)
        return result
'''
跟76， 159 一样的题
'''