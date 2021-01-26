class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]].append(i)
            else:
                dic[nums[i]] = [i]
        max_number = float("-inf")
        result = float("inf")
        for i in dic.values():
            max_number = max(max_number, len(i))

        for i in dic.values():
            if len(i) == max_number:
                result = min(result, (i[-1] - i[0]) + 1)
        return result
'''
创建字典
遍历数组 把每个数组 对应的 出现过的index 全部放进字典中 这样我们就可以直到 每个数字在哪几个index出现了 注意 value是一个有 所有index的list
然后 查找字典的 values 求出 最长的values 
求出以后 再次遍历字典 
如果发现 每个value list的长度 跟 max number一样的话 我们就用list中最后一个元素 减去 第一个元素 加1 出现最多次数之一元素的长度
然后还要跟之前的result 进行比较
'''
if __name__ == "__main__":
    soluiton = Solution()
    print(soluiton.findShortestSubArray([1,2,2,3,1]))