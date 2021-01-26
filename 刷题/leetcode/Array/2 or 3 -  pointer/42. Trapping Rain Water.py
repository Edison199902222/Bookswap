class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        water_area = 0
        left = 0
        right = len(height) - 1
        left_max = height[left] # 左边最高的柱
        right_max = height[right] # 右边最高的柱子
        while left <= right:
            # 每次比较 左边大 还是右边大，从较小的地方开始灌水
            if left_max <= right_max:
                # 灌水时，先比较当前柱子跟最大值柱子的大小，如果比最大值大，我们不能灌水
                if height[left] > left_max:
                    left_max = height[left]
                    left += 1
                    continue
                water_area += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    # 灌水时，先比较当前柱子跟最大值柱子的大小，如果比最大值大，我们不能灌水
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

'''
用单调栈的解法 有点像84 题
'''


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        area = 0
        # 只有两边都高于 中间的，我们才能灌水，然后由两边较小的那个进行灌水，所以stack需要保持递减
        for right in range(len(height)):
            while stack and height[right] > height[stack[-1]]:
                target_index = stack.pop()
                # 如果找不到左边界的话，说明当前index 无法灌水
                if not stack:
                    continue
                # 确定左边界
                left_bound = stack[-1]
                # 从矮的一方 往里面灌
                height_min = min(height[right], height[left_bound])
                # 要灌的距离 是两个 边界的距离
                area += (height_min - height[target_index]) * (right - left_bound - 1)
            stack.append(right)
        return area

