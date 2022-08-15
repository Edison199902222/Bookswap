class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # 第一步 创建 字典， key 是出现过的字母， value 是 字母所对于出现的位置，从第一次出现 到最后一次出现
        dic = collections.defaultdict(list)
        for i in range(len(s)):
            dic[s[i]].append(i)
        # 第二步， 筛选所有符合第二个条件的substring， 记录下对应的开始位置 到结束位置
        for char in dic:
            start = dic[char][0]
            end = dic[char][-1]
            temp_start = start
            temp_end = end
            while True:
                # 对当前字母的substring， 扩大所有区间 直到里面出现的所有字母 都只出现在当前substring中
                for c in set(s[start:end + 1]):
                    temp_start = min(temp_start, dic[c][0])
                    temp_end = max(temp_end, dic[c][-1])
                if temp_start == start and temp_end == end:
                    break
                start = temp_start
                end = temp_end
            dic[char] = [start, end]
        # 第三步， 以substring 结束的index 来进行排序，因为结束得越早，代表越有可能后面有越多的substring
        # 看作区间的话， 区间结束的越早，后面就会有越多的空位 留给可能的区间
        end_range = sorted(dic.values(), key=lambda x: x[1])
        result = []
        prev = -1
        for start, end in end_range:
            if start >= prev:
                result.append(s[start:end + 1])
                prev = end
        return result
