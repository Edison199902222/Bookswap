import heapq


class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        dic = {}
        result = []
        for i in items:
            id = i[0]
            mark = i[1]
            if id not in dic:
                dic[id] = [mark]
                heapq.heapify(dic[id])
            else:
                heapq.heappush(dic[id], mark)
                if len(dic[id]) > 5:
                    heapq.heappop(dic[id])
        for id, mark_list in dic.items():
            mark = sum(mark_list) // 5
            result.append([id, mark])
        return result
'''
遍历items
然后如果发现id 不在dic中 那么把id作为key 放进dic中 value 需要heapify
如果发现 已经在dic中 我们先把mark 放进相应的value list中， 并且检查 value list 长度是否大于5 因为我们只需要五个最大值
如果超过五了 那么我们需要pop一个出来
最后再遍历字典
把mark算出来
'''