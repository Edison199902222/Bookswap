class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        sets = set()
        min_length = float("-inf")
        right = 0
        for left in range(len(s)):
            while right < len(s) and s[right] not in sets:
                sets.add(s[right])
                right += 1
            min_length = max(min_length, right - left)
            sets.remove(s[left])
        return min_length if min_length != float("-inf") else 0
'''
模版题 
窗口移动
用set 去检查 当前窗口是否有重复元素
'''