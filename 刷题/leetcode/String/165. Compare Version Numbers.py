class Solution(object):
    def compareVersion(self, version1, version2):
        v1 = version1.split(".")
        v2 = version2.split(".")
        for i in range(max(len(v1), len(v2))):
            if i < len(v1):
                num1 = int(v1[i])
            else:
                num1 = 0
            if i < len(v2):
                num2 = int(v2[i])
            else:
                num2 = 0
            if num1 < num2:
                return  - 1
            if num1 > num2:
                return 1
        return 0
if __name__ == '__main__':
    solution = Solution()
    print(solution.compareVersion("1.01","1.001"))
'''
先把 点去掉
然后遍历两个数组中 长的那个
然后把每一个字符都变成数字 
进行比较 注意 在变成数字前 需要先检查 当前index是不是有效的 因为我们循环时 遍历的是比较长的那个 所以有可能超过index
比较 小于 大于的情况
最后 如果一直相等 reutnr 0
'''