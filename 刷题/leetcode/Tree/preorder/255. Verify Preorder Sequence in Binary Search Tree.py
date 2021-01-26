class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack = []
        min_value = float("-inf")
        for i in preorder:
            # 当前node 不应该小于 任何一个 min value
            # min value 是 左子树的最大值
            if i < min_value:
                return False
            # 如果当前值大于stack top元素， 说明某个node 的右子树出现了
            # 用while 找到这个右子树 属于哪个node 来更新min
            # 之后的所有元素， 都不能小于min
            while stack and i > stack[-1]:
                min_value = stack.pop()
            stack.append(i)
        return True

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        # 替代stack stack[:index]
        index = 0
        min_value = float("-inf")
        for x in preorder:
            if x < min_value:
                return False
            # index > 0 相当于 stack 不为空
            # 当前元素 如果 大于 index -1， index -1 相当于 top 元素
            # index -= 1 相当于pop出
            while index > 0 and x > preorder[index - 1]:
                min_value = preorder[index - 1]
                index -= 1
            # 相当于添加x 进stack
            preorder[index] = x
            index += 1
        return True