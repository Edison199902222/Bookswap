from heapq import heappop, heappush
'''
用扫描线的方法
将每个矩形的左右两边 分为两个事件
左边记录 x坐标 True 高度 跟 index
右边记录 x坐标 false 高度 跟index
然后按照x坐标进行排序
然后扫描
创建一个 set end 去储存不再有效的高度的index
如果遇到左边的 那么我们就把高度放进heap中
遇到右边 就把index 放进set中
我们用set的方法 来删除
首先我们检查 当前heap有没有过期的高度 也就是检查 heap中最高高度的id 是不是在end中
如果在的话 我们就不断pop 直到最高高度没有过期
然后如果我们发现 result中 有两个x是重合的， 我们需要把前面的那个pop出来
然后我们要判断 什么时候 是key point 然后添加进result
首先 如果result 是空的话， 那么当前的坐标 肯定是key point
第二 如果maxheap中有最高高度， 我们发现 当前的最高点的高度与前一个 坐标的高度 不一样， 说明是一个拐点 也是一个key point
第三 如果没有maxheap中没有东西了，也就是所有高度都过期了 那说明我们要添加 x，0 这也是一个keypoint
'''
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 首先，key point 是取决于当前扫描的区间内最高的高度， 所以之后用heap记录当前区间内的最大值
        event = []
        # 分类，把start 跟 end 分开，并且带上index，以便后面检查高度是否过期
        for index, points in enumerate(buildings):
            event.append([points[0], True, points[2], index])
            event.append([points[1], False, points[2], index])
        # 要sort，从左到右 按照坐标轴的顺序
        event.sort()
        heap = []
        pop_index = set()
        result = []
        # 对于每一个x，heap 维持当前最高高度
        # 要确定是key point，首先先检查当前高度是否过期，过期加入set中，并且把heap中过期的高度最大值pop
        # 第二 检查当前高度 跟 前一个key point 的高度是否一样
        # 确定当前的 x 是key point，结合当前最高高度 放进result中
        for point in event:
            x, flag, y, id = point
            if flag:
                heapq.heappush(heap, (-y, id))
            else:
                pop_index.add(id)
            while heap and heap[0][1] in pop_index:
                heapq.heappop(heap)
            if result and result[-1][0] == x:
                result.pop()
            if not result:
                result.append([x, -heap[0][0]])
            elif not heap:
                result.append([x, 0])
            elif -heap[0][0] != result[-1][1]:
                result.append([x, - heap[0][0]])
        return result
if __name__ =="__main__":
    Solution = Solution()
    print(Solution.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))