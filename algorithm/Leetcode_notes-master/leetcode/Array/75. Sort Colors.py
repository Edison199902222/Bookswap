
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        index = self.partition(nums, 0, len(nums), 0)
        self.partition(nums, index, len(nums), 1)
        return nums

    def partition(self, nums, left, right, pivot):
        i = left
        for j in range(left, right):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return i

'''
三分快速排
建立首尾双指针left和right，分别指示0/1边界和1/2边界

left左边（不含left）全为0，right右边（不含right）全为2
我们要用三个指针
left 指向 左边都是0 不是0的第一个数字
right 从后往前 指向 右边都是2 不是2的第一个数字
然后 mid 指针 指向 第一个指针开始 如果这个数字 是1 的话 则跳过
如果是0的话 就和第一个指针交换 两个指针+1， 因为left 和 mid 一起动，所以left 指向的肯定是1或者0， 如果是0 的话 交换以后 left += 1，mid 变成 0 也需要 + 1 不然会死循环 
如果是2的话 就和right 交换 第二个指针-1 但是 mid不能动 因为我们并不知道第二个指针指向的数字是什么， 有可能是 0 1 2 任意一个
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        mid = 0
        while mid <= right:
            if nums[mid] == 1:
                mid += 1
            elif nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 2:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1
        return nums
'''
为什么 mid = 0的时候， mid 要 +=1， 而 mid = 2的时候不用呢？
是因为mid 左边的值已经扫描过了，所以mid要++继续扫描下一位，而与right交换的值，mid 还没扫描，要停下来扫描一下，所以mid不用++。

虽然curr左边的都扫描过了，但是如果交换过来的是一个0，而且0左侧有1存在呢（实际上这种情况不存在，但是我们应该弄清楚为什么它不存在）？
我认为这里其实应该是分情况讨论。当nums【curr】==0的时候，有两种情况：
① left< curr，这种情况下 nums【left】==1（因为只有遇到了1之后，p0和curr才会拉开距离），那么交换之后就可以直接curr++ ② left==curr，这种情况下，显然也应该直接右移，即curr++。
'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 3 - way partition
        # 维护三个指针， 0 到 left - 1 是小于等于 key 的值
        # left 到 cur - 1 是等于key
        # cur 到 right 是未知
        left = 0
        right = len(nums) - 1
        cur = 0
        # cur 一直走，一直检查，直到跟right相遇
        while cur <= right:
            # 如果小于1，放在left，并且同时走一步，left 也可以走是因为 对于left 指向的 是等于 cur 的值，我们已经检查过了
            if nums[cur] < 1:
                nums[left], nums[cur] = nums[cur], nums[left]
                left += 1
                cur += 1
            # cur 不能+ 1，是因为right 交换过来的值我们是未知的，所以要多检查一轮
            elif nums[cur] > 1:
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1
            else:
                cur += 1