class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        result = []
        p = [i for i in range(1, m + 1)]
        for i in range(len(queries)):
            index = p.index(queries[i])
            result.append(index)
            p = [p[index]] + p[:index] + p[index + 1:]
        return result

'''
切片！！

'''
