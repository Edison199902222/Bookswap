class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
用一个队列
每次把一层 添加进去并且带上level（node，level）
并且遍历 这一层的 如果发现level是奇数那么就正常添加进list
如果是偶数 则每次加在第一位
每次并且把node 左右孩子添加进queene里面

'''
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return
        res, queene = [], []
        queene.append((root, 1))
        while queene:
            length = len(queene)
            nodeList = []
            for i in range(length):
                node, level = queene.pop(0)
                if level % 2 == 1:
                    nodeList.append(node.val)
                else:
                    nodeList.insert(0, node.val)
                if node.left:
                    queene.append((node.left, level + 1))
                if node.right:
                    queene.append((node.right, level + 1))
            res.append(nodeList)
        return res
if __name__=='__main__':
    solution=Solution()
    A1 = TreeNode(1)
    A2 = TreeNode(2)
    A3 = TreeNode(3)
    A4 = TreeNode(4)
    A5 = TreeNode(5)

    A1.left=A2
    A1.right=A3
    A2.left=A4
    A2.right=A5
    print(solution.zigzagLevelOrder(A1))