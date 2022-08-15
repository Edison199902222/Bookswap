class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        dic = collections.Counter()
        left = 0
        length = 0
        count = 0
        for right in range(len(tree)):
            dic[tree[right]] += 1
            if dic[tree[right]] == 1:
                count += 1
            while count >= 3:
                dic[tree[left]] -= 1
                if dic[tree[left]] == 0:
                    count -= 1
                left += 1
            if right - left + 1 > length:
                length = right - left + 1
        return length
'''
实际上是一个窗口问题
意思是 求出 最长的window， window里面的不同的数不能超过2 个
'''