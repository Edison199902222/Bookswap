class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        total_area = (C - A) * (D - B) + (G - E) * (H - F)
        if E > C or F > D or A > G or B > H:
            return total_area
        left = max(A, E)
        right = min(C, G)
        upper = min(D, H)
        down = max(B, F)
        return total_area - (right - left) * (upper - down)
'''
我们先算出 两个 矩形 一共的面积
然后 判断 如果没有 交集的话 ， 也就是 第二个矩形的左下 大于 第一个的右上 跟 第一个的左下 大于第二个的右上的话 直接return 一共的面积
如果有交集 那么我们观察图像可以知道
'''