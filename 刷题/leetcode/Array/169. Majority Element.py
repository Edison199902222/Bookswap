'''
用字典去计数
时间是 o（n）
'''
class Solution:
    def majorityElement(self, nums) -> int:
        dic = {}
        count = len(nums)//2
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] = dic.get(nums[i])+1
            else:
                dic[nums[i]] = 1
        max_value = max(dic,key = dic.get)
        max_count = dic[max_value]
        if max_count > count:
            return max_value
if __name__ == '__main__':
    solution = Solution()
    list = [1,2,3,4,1,1,1]
    print(solution.majorityElement(list))