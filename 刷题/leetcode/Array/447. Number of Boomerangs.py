class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = 0
        for x1, y1 in points:
            dic = {}
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                dx = x1 - x2
                dy = y1 - y2
                d = dx ** 2 + dy ** 2
                if d in dic:
                    result += dic[d]
                    dic[d] += 1
                else:
                    dic[d] = 1
        return result * 2
'''
两层遍历 
记录其他点 与当前点的距离
如果距离 已经存在于字典中 说明可以组成一个三个点的数组
那么我们 结果 进行加上 之前这个距离的次数 然后在 字典中出现的距离 加1 
如果 距离 没有存在字典中 那么就放进字典里
最后result 要乘 2 因为两个点顺序不一样 算不一样
'''