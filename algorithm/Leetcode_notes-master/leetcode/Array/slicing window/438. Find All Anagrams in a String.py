'''
滑动窗口
先把p中每个字符出现的次数放进字典里
然后两个指针遍历字符串s
同时用count记录当前串是否完成匹配，count主要是记录字典的统计信息的，这样就不用去遍历字典检查信息了。
end指针先动 一旦发现 字符在字典里 那么字符出现次数就-1
如果发现count == 0 的时候 那么我们就移动begin指针 去一步步缩小范围 一旦发现跟p的长度是一样 就说明这串字符串就是匹配p的
'''


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return
        counter = collections.Counter(p)
        count = len(counter)
        left = 0
        result = []
        for right in range(len(s)):
            if s[right] not in counter:
                continue
            counter[s[right]] -= 1
            if counter[s[right]] == 0:
                count -= 1
            while count == 0:
                if s[left] not in counter:
                    left += 1
                    continue
                if right - left + 1 == len(p):
                    result.append(left)
                counter[s[left]] += 1
                if counter[s[left]] == 1:
                    count += 1
                left += 1
        return result


if __name__ == "__main__":
    soluiton = Solution()
    print(soluiton.findAnagrams("cbaebabacd","abc"))