class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        # 每一层 对应 pattern 的一个字母
        # 尝试去遍历 str 的 start 到 end， 去尝试匹配当前pattern 的字母
        # 两个 hashmap 对应 pattern 跟 str 的映射
        return self.dfs(pattern, str, {}, {}, 0, 0)

    def dfs(self, pattern, str, p_dic, s_dic, i, j):
        # 如果 两个字符串都走到尾部，肯定是匹配完成
        if i == len(pattern) and j == len(str):
            return True
        if i == len(pattern) or j == len(str):
            return False
        cur_pattern = pattern[i]
        # 遍历当前string 的 start 到end，去尝试建立对的映射关系
        for index in range(j, len(str)):
            cur_string = str[j: index + 1]
            # 如果cur pattern 已经出现过，并且之前的映射关系跟现在的cur string 不匹配
            if cur_pattern in p_dic and p_dic[cur_pattern] != cur_string:
                continue
            # 如果cur string 已经出现过，并且之前的映射关系跟当前层的 pattern 不匹配
            if cur_string in s_dic and s_dic[cur_string] != cur_pattern:
                continue
            new_p = {k: v for k, v in p_dic.items()}
            new_s = {k: v for k, v in s_dic.items()}
            new_p[cur_pattern] = cur_string
            new_s[cur_string] = cur_pattern
            if self.dfs(pattern, str, new_p, new_s, i + 1, index + 1):
                return True
        return False