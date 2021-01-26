class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        left = 0
        right = 0
        for sh in shift:
            if sh[0] == 0:
                left += sh[1]
            else:
                right += sh[1]

        if right == left:
            return s
        elif right > left:
            net = (right - left) % len(s)
            return s[-net:] + s[:-net]
        else:
            net = (left - right) % len(s)
            return s[net:] + s[:net]

'''
先遍历一遍
算出 左移 跟右边 移动的数量
然后判断 哪个比较大
我们往数字比较大的 那个方向移动 
'''