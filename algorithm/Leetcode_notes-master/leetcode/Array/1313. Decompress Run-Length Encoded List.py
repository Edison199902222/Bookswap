'''
这道题意思是
【1，2，3，4】
这个含义是 一个2 三个四
output应该是 【2，4，4，4】
'''



class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0,len(nums),2):
            fre = nums[i]
            value = [nums[i+1]]
            res.extend(value*fre)
        return res

