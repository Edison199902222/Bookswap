'''
同向双指针
用两个指针 slow fast记录
matchcount 用来检查 从slow 到 fast 里面是不是含有我们所有的t
字典就是用来记录 t之中 所有字母出现的次数
一旦字典中全部为0 那么就说明我们找齐了
然后用指针 开始遍历s
如果指针指向的不在我们的字典中 说明不满足目标 那么就跳过
如果在的话 那么目标出现的次数就要-1
这时候检查 这个字典的这个字母 是不是等于 0 如果等于0 就说明我们满足了一个字母出现的次数
再检查 是否matchount 等于我们 t的长度
如果相等的话 那说明我们找齐了
那就slow指针开始动 如果这个slow指向的字母 在字典中 那么我们就加1

'''
import collections


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ""
        dic = {}
        for i in range(len(t)):
            if t[i] not in dic:
                dic[t[i]] = 1
            else:
                dic[t[i]] += 1
        slow = 0
        minlen = float('inf')
        matchcount = 0
        index = 0
        for fast in range(len(s)):
            if s[fast] not in dic:
                continue
            dic[s[fast]] -= 1
            count = dic[s[fast]]
            if count == 0:
                matchcount += 1
            while matchcount == len(dic):
                if fast - slow + 1 < minlen:
                    minlen = fast - slow + 1
                    index = slow
                leftchar = s[slow]
                slow += 1
                if leftchar not in dic:
                    continue
                dic[leftchar] += 1
                if dic[leftchar] == 1:
                    matchcount -= 1
        if minlen == float("inf"):
            return ""
        else:
            return s[index:index + minlen]


class Solution(object):
    def minWindow(self, s, t):
        counter = collections.Counter(t)
        count = len(counter)
        left = 0
        length = float("inf")
        index = 0
        for right in range(len(s)):
            if s[right] not in counter:
                continue
            counter[s[right]] -= 1
            if counter[s[right]] == 0:
                count -= 1
            if count != 0:
                continue
            while count == 0:
                if right - left + 1 < length:
                    length = right - left + 1
                    index = left
                if s[left] not in counter:
                    left += 1
                    continue
                counter[s[left]] += 1
                if counter[s[left]] == 1:
                    count += 1
                left += 1
        return s[index:index + length] if length != float("inf") else ""
if __name__ == '__main__':
    solution = Solution2()
    print(solution.minWindow("ADOBECODEBANC","ABC"))