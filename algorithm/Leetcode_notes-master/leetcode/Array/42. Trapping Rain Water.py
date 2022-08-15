class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        water_area = 0
        left, right = 0, len(height) - 1
        left_max = height[left]
        right_max = height[right]
        while left <= right:
            if left_max < right_max:
                if height[left] > left_max:
                    left_max = height[left]
                    left += 1
                    continue
                water_area += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                    right -= 1
                    continue
                water_area += right_max - height[right]
                right -= 1
        return water_area

'''
我们从两边往里面灌水
先得到 最左边柱子高度 与最右边柱子高度 
我们每一次需要比较
如果左边柱子最大值的高度 矮 那么我们就从左往右灌水
如果右边柱子最大值的高度 矮 那么我们从右往左灌水
因为 矮的那么一边 奠定了灌水最高能灌多高 因为如果有柱子 比 矮的那么一边高的话 水会溢出

然后我们遍历
先判断 我们left_max right_max谁小 我们从哪开始灌
然后 我们用再判断 如果当前的柱子 超越我们 矮的那一边的柱子的话 说明无法灌水， 但是我们可以更新 max值 并且指针加1
如果没有超越矮的那一边的柱子的话， 那么我们就可以灌水了 我们用 矮的那一边的柱子 减去当前柱子的高度 就会等于 可以灌多少
然后移动指针
'''