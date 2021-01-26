class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return 0
        dic = {}
        result = 0
        for i in range(len(arr)):
            if arr[i] not in dic:
                dic[arr[i]] = 1
            else:
                dic[arr[i]] += 1
        for key, val in dic.items():
            if key + 1 in dic:
                result += val

        return result
'''
关键就是 怎么理解正确的计数
我们需要找到 如果数组中存在当前数字 + 1的话
那么我们就加上 当前数组的数量就行了
'''