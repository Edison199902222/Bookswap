class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dic = collections.Counter()
        for i in cpdomains:
            times, web = i.split()
            dic[web] += int(times)
            for j in range(len(web)):
                if web[j] == ".":
                    dic[web[j + 1:]] += int(times)
        result = []
        for key, values in dic.items():
            temp = str(values) + " " + key
            result.append(temp)
        return result
'''
先创建一个字典
然后遍历给定的数组
用split 把每一个 访问的次数 跟 网站分开
然后把网站 跟访问次数 先放进字典中
然后遍历网站 
如果遇到 点 的话 我们就切片 去掉从头到当前index的 并且把访问次数 放进字典中
遍历结束后 字典变成了一个所有域名 对应访问次数的字典
然后再遍历字典 放进result中

'''