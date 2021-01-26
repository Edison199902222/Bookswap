class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        j = 0
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return j == len(popped)
'''
stack 用来模拟整个过程
遍历pushed 每次压入一个元素进stack
并且 另一个指针j 指向pop 的元素 如果发现 stack中top 元素 与 j 指向的元素相同
那么我们就pop出 并且移动 j 指针
最后 我们检查 j 是否遍历完pop 数组 
其实就是一个 模拟push 跟 pop 的过程 
time： O(n)
space: O(n)
'''


class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        i = 0
        j = 0
        for value in pushed:
            pushed[i] = value
            while i >= 0 and pushed[i] == popped[j]:
                i -= 1
                j += 1
            i += 1
        return i == 0
'''
这是一个更好解法
我们有 三个指针
i 指向的是我们建立的stack value 指向的是pushed 中 当前要压入的元素
j 指向的是 要pop出去的元素
我们每一次 把value 压入 i 的stack 中， 用 指针i 的话 可以省去创建一个stack
然后 检查 如果当前stack 中 的top 元素 是等于 我们要pop出去的元素的话
那么我们就把它pop出去 也就是 我们i - 1 
并且 j + 1 指向下一个要pop出去的元素
然后 i + 1 进行下一次压入
最后我们检查 i 是否等于 0， 如果i 等于0 的话， 说明 整个stack 已经pop 出所有元素了
'''