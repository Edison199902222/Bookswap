class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        # 想要最接近当前数，并且小于当前数字
        # 那么我们更改的数字的位 越低越好 并且我们要找到如果有一位数字，右边有比它小的数字时，才能替换
        # 所以 我们从右往左找，找到第一个 它的右边有比它自己小的数
        # 并且我们如果找到要更改的数字的位，那么肯定最好找它右边最接近它的数字
        # 比如194691， 我们从后往前找，肯定是 9 跟 1 换位置，这样组成的数，最接近原数字
        index = len(A) - 2
        while index > - 1:
            # 找到需要更改的位置了
            if A[index] > A[index + 1]:
                # 找到它右边最接近它的数，交换位置
                j = pivot = index + 1
                # 如果找到比index 大的数字的话， 需要停止
                while j < len(A) and A[index] > A[j]:
                    # 找到 pivot < j < index 更新pivot 这才是最接近的数
                    if A[j] > A[pivot]:
                        # 只有比pivot 大才更新，如果相等的话，要使改变后的数字越接近原数字 要离当前index位越近越好
                        # 比如[3,1,1,3]我们希望 index 0 跟 index1 交换位置，而不是index 0 跟index2 交换
                        pivot = j
                    j += 1
                A[index], A[pivot] = A[pivot], A[index]
                break
            index -= 1
        return A
