'''
先用字典
把people list 的 身高作为key index 作为value
然后按照key从大到小排序 这样是因为待会插入result 的时候 直接按照k 插入 这样使得身高小的在前面 身高大的在后面
比如 （5，0） （7，0） index一样 但是5必须在前面
然后两个for遍历字典
遍历字典的时候 把value还要排序
排序后 直接用k插入

这个题怎么想出来的呢？是因为我们考虑如果先把个子高的排好序，那么在任何位置插入数据都不会对已经排好序的数组造成影响。
而，与此同时，我们已经知道了个子高的排序，那么当新的数据到的时候，我们要确定它的位置也很简单，因为现在的所有数据都比他高，
所以只要根据他的第二个数字确定他的位置即可。

先对已有的数组进行排序。按照高度降序排列，如果高度一样，按照k的值升序排列。
这样比如一开始[7，0] [7，1] [7，2]就会排好，然后比如说后面有一个[6，1]，
说明只有一个大于或等于它，又因为比6大的已经全部取出。所以把它放在位置1，这样就变成[7，0] [6，1] [7，1] [7，2].然后比如又有一个[5，0].就放在位置0，以此类推。

'''

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        dic = {}
        for i in people:
            h,k = i[0],i[1]
            if h not in dic:
                dic[h] = [k]
            else:
                dic[h].append(k)
        result = []
        for i in sorted(dic.keys(),reverse = True):
            dic[i].sort()
            for j in dic[i]:
                result.insert(j,(i,j))
        return result

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key = lambda x : (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res
4