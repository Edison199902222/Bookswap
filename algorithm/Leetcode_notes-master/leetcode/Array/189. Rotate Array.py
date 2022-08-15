'''
首先需要把k%list的长度
因为真正有效的k 是除余后的k 因为比如 list长度5 k为7 那么其实 k=2的 因为前五次是会变会原样
然后 先把list 旋转整体
在旋转k-1 个 因为k-1 才是index
再把后面 剩下的旋转了
'''
class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        self.reversed(nums,0,len(nums)-1)
        self.reversed(nums,0,k-1)
        self.reversed(k,len(nums)-1)



    def reversed(self,nums,start,end):
        while start <= end:
            nums[start],nums[end] = nums[end],nums[start]
            start+=1
            end-=1
if __name__ == "__main__":
    solution = Solution()