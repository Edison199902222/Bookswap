class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        # write your code here
        self.quick_sort(colors, 1, k, 0, len(colors) - 1)

    def quick_sort(self, colors, color_start, color_end, start, end):
        if start >= end or color_start >= color_end:
            return
        mid = (color_start + color_end) // 2
        pos = self.partition(colors, start, end, mid)
        self.quick_sort(colors, color_start, mid, start, pos)
        self.quick_sort(colors, mid + 1, color_end, pos + 1, end)

    def partition(self, colors, left, right, pivot):
        for i in range(len(colors)):
            if colors[i] == pivot:
                colors[i], colors[right] = colors[right], colors[i]
                break
        i = left
        for j in range(left, right):
            if colors[j] <= pivot:
                colors[i], colors[j] = colors[j], colors[i]
                i += 1
        colors[i], colors[right] = colors[right], colors[i]
        return i


'''
quick sort 的改版
如果区间中只有一个颜色的话，那么我们就停止排序
如果区间中有超过一个颜色的话， 我们每次选取 区间颜色中的中间颜色 mid
然后 把 小于等于 mid 的放在左边，右边放大于 mid的颜色
'''

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        counter = [0] * (k + 1)
        for i in range(len(colors)):
            counter[colors[i]] += 1
        index = 0
        for color, count in enumerate(counter):
            for _ in range(count):
                colors[index] = color
                index += 1
'''
counting sort
'''