class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for i in range(len(strings)):
            code = self.encode(strings[i])
            if code in dic:
                dic[code].append(strings[i])
            else:
                dic[code] = [strings[i]]
        return [value for value in dic.values()]

    def encode(self, string):
        if not string:
            return -1
        if len(string) == 1:
            return 1
        code = [0] * (len(string) - 1)
        for i in range(1, len(string)):
            code[i - 1] = (ord(string[i]) - ord(string[i - 1])) % 26
        return tuple(code)


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        # 用每一个string 的每个字母跟前一个字母的相对位置差值来作为标记
        # 如果是一样的话，就放在一个组里面
        for char in strings:
            diff = []
            for i in range(1, len(char)):
                diff.append((ord(char[i]) - ord(char[i - 1])) % 26)
            dic[tuple(diff)].append(char)
        result = []
        for i in dic.values():
            result.append(i)
        return result


'''
使用 字典 储存 code 相同的string
我们调用 encode 函数 
encode 作用是 把string 中 从第二位开始 算出与前一位的ord 差值！ 记得必须要 % 26， 因为 az 跟 ba这种 是一样的

'''