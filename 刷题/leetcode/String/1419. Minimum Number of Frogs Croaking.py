class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        c, r, o, a, k = 0, 0, 0, 0, 0
        in_use = 0
        result = 0
        for i in croakOfFrogs:
            if i == "c":
                c += 1
                in_use += 1
            elif i == "r":
                r += 1
            elif i == "o":
                o += 1
            elif i == "a":
                a += 1
            else:
                k += 1
                in_use -= 1
            if not (c >= r >= o >= a >= k):
                return - 1
            result = max(result, in_use)
        if c == r == o == a == k:
            return result
        return - 1
'''

相当于一个上车问题
每一次 c r o a k 上车 但 k 每一次上车了 前面的croa都要下车 问 同时几个c 在车上
并且车子行驶中 c的数量 必须是 在场人中最多或者相等其他人的 
'''


class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        dic = {croakOfFrogs[v]: 0 for v in range(len(croakOfFrogs) - 1)}
        result = -1
        for i in range(len(croakOfFrogs)):
            if croakOfFrogs[i] == "k":
                for key in dic.keys():
                    dic[key] -= 1
            else:
                dic[croakOfFrogs[i]] += 1
            if not (dic["c"] >= dic["r"] >= dic["o"] >= dic["a"]):
                return - 1
            result = max(result, dic["c"])
        if not (dic["c"] == dic["r"] == dic["o"] == dic["a"] == 0):
            return - 1
        return result
