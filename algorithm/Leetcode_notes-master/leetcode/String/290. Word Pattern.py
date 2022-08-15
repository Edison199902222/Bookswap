class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        string = str.split()
        dic = {}
        # 存在双向映射关系， 先检查pattern的
        if len(string) != len(pattern):
            return False
        for i in range(len(pattern)):
            # 如果还没记录的话， 那么把当前pattern 的字符 和 string 的字符 对应上来
            # 建立映射关系
            if pattern[i] not in dic:
                dic[pattern[i]] = string[i]
            # 如果之前已经出现过，查一下 现在string 的字符 是不是 跟之前pattern 对应的字符 一样的
            elif dic[pattern[i]] != string[i]:
                return False
        dic = {}
        # 检查string的
        for i in range(len(string)):
            # 建立映射关系
            if string[i] not in dic:
                dic[string[i]] = pattern[i]
            elif dic[string[i]] != pattern[i]:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    pattern = "abba"
    str = "dog cat cat dog"
    print(solution.wordPattern(pattern,str))