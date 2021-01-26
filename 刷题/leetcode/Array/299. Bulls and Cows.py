'''
cow 的意思是 有这个数字 但是位置错了 就算是cows
首先 用couter 去 计算secret 每个出现了多少次
然后 记录 bulls出现的次数 同时减去在counter中出现的次数
最后 再循环一次 记录cow的次数

整体思路就是：先计算出每个数字出现的次数
如果位置跟数字都对了 则 cows加1 并且 在字典中这个数字出现的次数减去一
然后再 计算bows 每个位置比较 如果不相等的话 则 guess中这个数字 还在 secret答案 中出现过 并且出现的次数大于0 才可以加1 
'''
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        if not secret:
            return "0A0B"
        check = collections.Counter(secret)
        bulls, cows = 0,0
        # check bulls
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bulls += 1
                check[guess[i]] -= 1
        # check cows
        for i in range(len(guess)):
            if guess[i] != secret[i]:
                if guess[i] in check and check[guess[i]] > 0:
                    cows += 1
                    check[guess[i]] -= 1
        return str(bulls) + "A" + str(cows) + "B"
