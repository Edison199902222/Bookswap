
'''
用一个hashtable 去储存magazine中出现的单词以及次数
然后遍历randsomnote 去查找 在hashrable里面有没有
'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hashmap = {}
        if len(ransomNote) > len(magazine):
            return False
        for i in magazine:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        for i in ransomNote:
            if i not in hashmap or hashmap[i] == 0:
                return False
            hashmap[i] -= 1
        return True
