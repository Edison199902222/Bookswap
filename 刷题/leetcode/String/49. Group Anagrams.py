'''
用字典
先遍历一遍list  然后每个字符串按字母顺序排序好 然后用排序好的字符串作为key 没排序的字符串作为value 添加进字典里
如果 字符串排序后 已经出现在字典里 那么就添加进value的list之中
最后把字典里的value 一个个添加进result之中
原理 其实就是 如果会分成一类的话 那么排序后的字符串 一定相同 用一定相同的字符串作为key 
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        if strs is None or len(strs) == 0: return result
        dic = {}
        for s in strs:
            current = list(s)
            current.sort()
            if str(current) not in dic:
                dic[str(current)] = [s]
            else:
                dic[str(current)].append(s)
        for i in dic.values():
            result.append(i)
        return result
if __name__ == "__main__":
    solution = Solution()
    string = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(string))