class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dic = collections.Counter(words)
        heap = []
        for word, value in dic.items():
            heapq.heappush(heap, (-value, word))
        result = []

        while heap and k > 0:
            result.append(heapq.heappop(heap)[1])
            k -= 1
        return result
'''
用一个最小堆
作 取反操作 
这样越大的放进堆里面就会越小 也就是如果pop的话 越大的就会越早出来
我们建立一个字典 里面放着 所有数字出现的频率
然后遍历字典 把频率取反 跟 对应的字符 作为tuple 放进heap中
然后 我们遍历heap
每次pop一个出来 直到pop出 k个就停止
'''