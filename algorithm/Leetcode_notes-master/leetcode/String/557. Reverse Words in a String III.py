class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        i = 0
        j = 0
        while j < len(s):
            if s[j] == " ":
                result.append(s[i:j][::-1])
                i = j + 1
                j += 1
            elif j == len(s) - 1:
                result.append(s[i:j+1][::-1])
                j += 1
            else:
                j += 1
        return " ".join(result)