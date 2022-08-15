class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []
        # 找到最大值，翻转，让其变成头
        # 然后再翻转整个数组，让它变成最后一个 剔除出去
        for i in range(len(A), 1, -1):
            index = A.index(i)
            # 变成头的操作
            result.append(index + 1)
            # 翻转整个数组的操作
            result.append(i)
            # 前面翻转了两次所以相对顺序不变，index后面只翻转了一次 顺序会变
            A = A[index + 1:][::-1] + A[:index]
        return result