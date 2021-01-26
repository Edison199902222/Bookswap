# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    def levelOrderBottom(self, root: TreeNode) :
        if not root:return []
        quene = [root]
        res = []
        while quene:
            res_temp = []
            for i in range(len(quene)):
                node = quene.pop(0)
                res_temp.append(node.val)
                if node.left:
                    quene.append(node.left)
                if node.right:
                    quene.append(node.right)
            res.insert(0,res_temp)
        return res




if __name__=='__main__':
    solution=Solution()
    A1 = TreeNode(3)
    A2 = TreeNode(9)
    A3 = TreeNode(20)
    A4 = TreeNode(15)
    A5 = TreeNode(7)

    A1.left=A2
    A1.right=A3
    A2.left=A4
    A2.right=A5
    ans=solution.levelOrderBottom(A1)
    print(ans)

