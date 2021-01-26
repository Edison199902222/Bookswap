class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        tail = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
            tail[i] = 0
        for i in nums:
            if dic[i] == 0:
                continue
            if i - 1 in tail and tail[i - 1] > 0:
                tail[i - 1] -= 1
                tail[i] += 1
            elif i + 1 in dic and i + 2 in dic and dic[i + 1] > 0 and dic[i + 2] > 0:
                dic[i + 1] -= 1
                dic[i + 2] -= 1
                tail[i + 2] += 1
            else:
                return False
            dic[i] -= 1
        return True
'''
首先统计好每个数字出现的次数
从最小的数字开始, 假设当前数字为num
先看看有没有数组以num - 1结尾, 有的话直接把num放过去, 然后以num - 1结尾的数组个数减1, 以num为结尾的数组的个数加1, num的频率减1, 继续下一个数字
如果以num - 1结尾的数组个数不够了, 说明需要建立新的数组,
 就要看num + 1和num + 2是否还有, 有的话就建立新的数组, 此时多了一个以num + 2结尾的数组, 所以num + 2结尾的数组个数加1, 同时num + 1, num + 2的频率减1, 最后num的频率也减1, 继续...
以上两点都不满足的话, 说明当前数字放不到任意一个已有的数组末尾, 并且也不能建立新的长度大于等于3的数组了, 返回False
'''