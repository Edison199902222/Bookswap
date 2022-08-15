# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        # 当前层的node
        temp = ""
        # stack 的长度 等于 当前层的深度
        stack = []
        # 计算 - 的数量
        depth = 0
        n = len(S)
        i = 0
        while i < n:
            # 先计算depth
            while i < n and S[i] == "-":
                depth += 1
                i += 1
            # 把当前node 放进temp
            while i < n and S[i].isdigit():
                temp += S[i]
                i += 1
            # 计算 depth 是否匹配当前深度， 不匹配的话 stack pop 直到匹配
            while stack and len(stack) > depth:
                stack.pop()
            node = TreeNode(int(temp))
            # 匹配后，看当前stack top 是缺了左孩子 还是右孩子
            if stack and stack[-1].left == None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            # 把stack放进node
            stack.append(node)
            depth = 0
            temp = ""
        return stack[0]