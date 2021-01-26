class Solution(object):
    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """
        Dict = {"&quot;": '"', "&apos;": "'", "&amp;": "&", "&gt;": ">", "&lt;": "<", "&frasl;": "/"}
        flag = False
        result = []
        temp = []
        for c in text:
            if c == "&":
                flag = True
                temp = []
                temp.append(c)
            elif flag:
                temp.append(c)
                if c == ";":
                    word = "".join(temp)
                    if word in Dict:
                        result.append(Dict[word])
                    else:
                        result.append(word)
                    flag = False
            else:
                result.append(c)
        if flag:
            result.append(temp)
        return "".join(result)
'''
用字典把对应string放好
然后遍历text
用flag 来检测 是否进入应该替换的状态
如果遇到 & 就说明 之后遇到的东西 有可能需要替换 
那么我们之后 每一次 都把 当前字符 放进temp中 并且检测 当前字符 是不是；
如果是 ；的话， 代表着结束  我们就需要检测 temp中的 string是不是 在替换字典中
如果有 就替换 没有 就把原 temp 放进result中 并且flag重新设置为false
遍历完以后 
还记得 如果flag是true的话 我们需要把结尾的部分放进去 因为有可能存在
Example: text = "harry & sally"
Your output = "harry & "
'''