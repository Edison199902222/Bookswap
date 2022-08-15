class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        # write your code here
        result = []
        answer = 0
        temp = 0
        for interval in airplanes:
            result.append([interval.start,1])
            result.append([interval.end, -1])
        result = sorted(result)
        for i in result:
            temp += i[1]
            answer = max(answer, temp)
        return answer
'''
扫描线经典题
把数组中起飞降落时间拆开， 用 1 跟 -1 标注
然后排序， 按照 时间的大小排序，注意 如果时间一样 那么就会按照第二个元素 的顺序进行排序，这样就保证了先降落的在前面
然后 我们遍历扫描线数组
每次遇到起飞就 + 1 降落就 - 1 用answer 一直去 追踪最大值
'''