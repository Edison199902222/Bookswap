# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        cadidate = 0
        for i in range(1, n):
            if knows(cadidate, i):
                cadidate = i
        for i in range(n):
            if i != cadidate and knows(cadidate, i):
                return - 1
            if i != cadidate and not knows(i, cadidate):
                return -1
        return cadidate
'''
每一次 我们调用 API 会出现两种情况
return True 如果 A 认识 B的话， 那也说明 A不是名人， 因为名人不能认识任何一个人
return False 如果 A 不认识B的话， 那也说明 B 不是名人， 因为名人会被所有人认识
所以 每一次 调用 Api 我们都可以 排除掉一个人 
所以 我们遍历数组，把候选人设置成0 号， 然后遍历从1 号 到最后一个人， 每一次问候选人 认不认识 第 i个人
如果认识的话，说明候选人不是名人， 我们把候选人换成i， 如果不认识的话， 说明 i不是名人， 候选人不变
 一共跑 n - 1次 就可以 排除掉n - 1 个不是名人的人
剩下的一个人 有可能是名人 所以我们再次遍历数组，询问其他所有人，不认识候选人 
并且询问候选人 认不认识其他人

'''