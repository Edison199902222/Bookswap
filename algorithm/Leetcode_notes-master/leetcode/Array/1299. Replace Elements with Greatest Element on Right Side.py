'''
从后往前遍历
last 目前这个数 右边的最大值
max——val 是为了更新 last 为下一个操作 保持最大值的
每次遍历一个数 先把max 赋给 last 因为每次 max 是保持这 当前数的最大值
然后 max 再跟目前数进行比较
再把last更新给 array
'''

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        max_val = -1
        for i in range(len(arr)-1,-1,-1):
            last = max_val
            max_val = max(max_val,arr[i])
            arr[i] = last
        return arr