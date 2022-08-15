class Solution(object):
    def canConvert(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        s1 = "ace", s2 = "cea", draw
        arrows
        between
        each
        transformation
        key  -> value
        a    ->    c
        c    ->    e
        e    ->    a
        # 这是一个cycle 因为 "a -> c -> e -> a"，所以我们需要一个varialble 去 让a 先暂时变成另一个
        # "a -> tmp" and "tmp -> c -> e -> a".这样，a就不会被后面的所影响
        # 所以我们必须要有一个variable才行，所以会检查str2的种类
        if str1 == str2:
            return True
        if len(str1) != len(str2):
            return False
        if len(set(str2)) == 26:
            return str1 == str2
        # 建立映射关系
        dic = {}
        for i in range(len(str1)):
            # 如果当前字符还未出现过，那么建立映射关系
            if str1[i] not in dic:
                dic[str1[i]] = str2[i]
            # 如果出现过，检查之前的映射关系 是否跟现在的字母是对上的
            else:
                if dic[str1[i]] != str2[i]:
                    return False
        return True

