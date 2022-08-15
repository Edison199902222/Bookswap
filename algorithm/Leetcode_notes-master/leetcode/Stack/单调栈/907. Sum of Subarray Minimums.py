class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        if not A:
            return 0
        stack = []
        A = [0] + A + [0]
        result = 0
        for i in range(len(A)):
            # 维护一个递增的stack
            while stack and A[i] < A[stack[-1]]:
                target_index = stack.pop()
                left_bound = stack[-1]
                # 左右边界确定了， 左右两个数字都小于 当前target
                # 说明 我们在 (left, right)这个距离内 是最小的数
                # 我们计算 我们可以以当前target 为最小数得到的连续子数组的组合有多少个
                # 数学上来说， 只需要找排列组合的问题， 我们先分裂成两个为题，以当前target 到 right， 可以组合多少个连续并且包含target 的子数组
                # 第二个 以当前target 到left 可以组合多少个连续并且包含target 的子数组
                # 这两个问题只需要，target - left 的index， 跟right - target index 就能知道
                # 因为target - left 表示 left 到target 除去left边界 有几个数， 比如 1 2 3， 3 是我们target 值
                # 那么连续包含target 的就是 3， 23， 123， 其实就是1 ～ 3 有几个数字
                # 然后我们求出 target的左边 跟 右边 必须包含target并且连续 的 子数组后，我们就可以转化成排列组合问题
                # 左边的组合 ✖️ 右边的组合， 就是从左边界到右边界必须包含target 的连续子数组的组合
                # 再乘以 target的值，我们就求出 以target为最小值，能贡献多少个 这样的target 值
                result += A[target_index] * (target_index - left_bound) * (i - target_index)
            stack.append(i)
        return result % (10**9 + 7)
'''
先在数组中 前后加0
这样我们可以防止找不到左右边界的问题
我们用stack 去维持一个单调递增的数组
stack的栈顶元素 是当前数字 的左边边界 
我们每次检查 只要当前元素大于stack中的栈顶元素
我们就放进stack中
一旦遇到 小于stack栈顶的元素 
把此时栈顶元素pop出来
我们就知道 当前元素 是pop元素的右边界
那么左边界就是 此时的栈顶元素
我们再用公式 右边界 减去 pop元素index ✖ pop元素index 减去 左边界 这就是以pop元素为最小值得到的连续子数组的组合种类

'''