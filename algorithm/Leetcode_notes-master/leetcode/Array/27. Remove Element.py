
'''
双指针
如果有就交换头尾 然后尾部往前移动一个
如果没有 头就移动
最后return end+1 因为一开始end-1 是整个list的长度 end移动了几次 就说明有几个一样的
'''
class Solution:
    def removeElement(self, nums, val: int) -> int:
        if not nums : return 0
        length = len(nums)
        start = 0
        end = length-1
        while start <= end:
            if nums[start] == val:
                nums[start],nums[end] = nums[end],nums[start]
                end-=1
            else:
                start+=1
        return end+1
if __name__ == "__main__":
    solution = Solution()
    nums = [3,2,2,3]
    length = solution.removeElement(nums, 4)
    print(nums[:length])