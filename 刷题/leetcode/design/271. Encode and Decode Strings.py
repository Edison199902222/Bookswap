class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        # 加密 以 冒号 + 空格来辨别
        # 如果遇到冒号， 让它变成两个冒号，因为我们是以冒号+空格来加密每一个string
        result = []
        for string in strs:
            for char in string:
                if char == ":":
                    result.append("::")
                else:
                    result.append(char)
            # 每一个单词结尾，加上冒号 + 空格 证明 结束
            result.append(": ")
        return "".join(result)

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        result = []
        temp = []
        i = 0
        while i < len(s):
            # 如果遇到冒号，则还要判断下一个是什么，来判断到底是结束，还是只是冒号
            if s[i] == ":":
                if s[i + 1] == ":":
                    temp.append(":")
                    i += 2
                elif s[i + 1] == " ":
                    result.append("".join(temp))
                    temp = []
                    i += 2
            else:
                # 没有遇到冒号直接放进temp中
                temp.append(s[i])
                i += 1
        return result


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
'''
encode 函数 把字符串array 用：加 空格的形式分割开！ 如果遇到： 我们就变成：：
decode 函数 把连续字符串 如果遇到： 我们就有两种情况， 一种是 ：的下一个字符也是： 这就说明， 原本的字符是一个， 把： 添加进temp中
如果下一个字符是 空格的话 说明 这就到我们一个string的结尾了， 那么把 temp中的字符 合并起来放进result
如果遇到的不是 ：， 直接放进temp中
'''
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))