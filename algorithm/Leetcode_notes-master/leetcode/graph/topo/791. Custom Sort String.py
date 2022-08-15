
'''
naive
'''
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        in_degree = {i: 0 for i in S}

        for i in range(len(S) - 1):
            in_degree[S[i + 1]] += 1

        result = ""
        count = collections.Counter(T)

        order_list = sorted(in_degree, key=lambda x: in_degree[x])
        for char in order_list:
            if char in count:
                result += char * count[char]
                count[char] = 0
        for char in count:
            if count[char] != 0:
                result += char * count[char]

        return result


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        result = ""
        count = collections.Counter(T)
        # 直接遍历s， 把s 看成in_degree的表
        for char in S:
            if char in count:
                result += char * count[char]
                count[char] = 0
        for char in count:
            if count[char] != 0:
                result += char * count[char]

        return result






