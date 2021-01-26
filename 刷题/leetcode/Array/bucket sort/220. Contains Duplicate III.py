class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0: return False
        dic = {}
        # 确定桶子的范围， w 表示一个桶子最多有几个数
        w = t + 1 # 防止待会桶排序时，x/w, w等于0
        # 加1 后，每一个桶子的左右边界，都是在t之内的的，差 最多等于t， 比如 t = 3， w = 4， 那么桶子的范围是 0 到 3， 有四个数
        for i in range(len(nums)):
            # 分配桶子的标号
            m = nums[i] // w
            if m in dic:
                return True
            # 还需要跟前后比较
            elif m + 1 in dic and abs(nums[i] - dic[m + 1]) < w:
                return True
            elif m - 1 in dic and abs(nums[i] - dic[m - 1]) < w:
                return True
            dic[m] = nums[i]
            #超过的index 去掉
            if i >= k: del dic[nums[i - k] / w]
        return False
'''
类似于桶排序
这道题 我们相当于建立很多个桶子
每一个桶子有一定的范围 比如第一个桶子范围是0到4 第二个桶子范围是5到8
然后把每一个数字放进桶子里，如果发现桶子里有数 说明有两个差值小于t 的出现了
我们是如何建立桶子的呢？ 
我们创建一个w， w 是等于 最大差值t + 1
任何数落在t+1的自己bucket 里他们的difference abs一定小于等于t 例如说t=3 bucket 1里的数就是 4,5,6,7 你看里面任何一个数相减的abs都是小于等于3的
如果超出k 需要减去之前的数
'''