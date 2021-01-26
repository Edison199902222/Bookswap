'''
两个指针
一个从头往后 一个从后往前
先算面积
然后 如果左边大于右边 右边往前挪
因为在两个height之中 我们永远想保留的是 height比较高的那个
'''


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        water_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] <= height[right]:
                water_area = max(water_area, (right - left) * height[left])
                left += 1
            else:
                water_area = max(water_area, (right - left) * height[right])
                right -= 1
        return water_area
