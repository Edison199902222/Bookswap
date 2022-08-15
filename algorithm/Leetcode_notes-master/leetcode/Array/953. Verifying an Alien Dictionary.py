class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dic = {}
        for i, char in enumerate(order):
            dic[char] = i
        for i in range(1, len(words)):
            pre_word = words[i - 1]
            cur_word = words[i]
            flag = False
            for j in range(min(len(pre_word), len(cur_word))):
                if dic[pre_word[j]] < dic[cur_word[j]]:
                    flag = True
                    break
                elif dic[pre_word[j]] > dic[cur_word[j]]:
                    return False
            if not flag and len(cur_word) < len(pre_word):
                return False
        return True
'''
先把order的所有字符 跟 对应的 index 放进 字典中
然后第一遍 从words 的 第二个单词开始遍历
设置 pre 用来 记录之前的单词
flag 记录 如果前面的单词的字符的顺序 在 当前单词的字符之前的话 
我们的flag 变成 true 并且 后面的字符不用比较了 因为顺序是对的
如果遍历完 flag 还是false的话 说明 单词每一个都相等 
第二遍遍历 跟 之前一个单词比较
每次比较 各自的每一个字符 是不是cur 的字符顺序 在pre 指向的字符 顺序 后面
如果是后面 flag = true 并且break
如果 pre的字符顺序 在 cur字符顺序后面的话 直接return false

第二遍 遍历完成以后 我们还需要检查 flag 是不是 false
如果是false 说明 两个单词 的字母是一样 那么我们就需要检查 cur的长度是不是比前一个单词短 
如果短的话 那么 return false
'''