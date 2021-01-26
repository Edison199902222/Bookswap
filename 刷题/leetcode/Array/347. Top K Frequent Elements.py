'''
先创造一个字典
然后把出现的次数跟值放进去
然后创造一个桶 每个桶的含义是 相同出现次数的数字放在一起
最后倒叙遍历array
从后往前看每个桶有没有数字 
'''

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        data, res = {}, []
        for i in nums:
            if i not in data:
                data[i] = 1
            else:
                data[i]+=1
        bucket = [[]for i in range(len(nums)+1)]
        for key in data:
            bucket[data[key]].append(key)
        for i in range(len(nums),-1,-1):
            if bucket[i]:
                res.extend(bucket[i])
            if len(res) >= k:
                break
        return res[:k]
if __name__ == "__main__":
    soluiton = Solution()
    print(soluiton.topKFrequent([1,1,2,2,3,3],1))