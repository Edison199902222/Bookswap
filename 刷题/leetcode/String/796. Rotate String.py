class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B:
            return True
        if len(A) != len(B):
            return False
        for i, char in enumerate(A):
            if char == B[0]:
                left_substring = A[:i]
                right_substring = A[i:]
                if right_substring + left_substring == B:
                    return True
        return False
'''
遍历A 我们先找到 A中与B第一个字母相等的指针i
然后 接下来 切片 把 i的左右两边 切成两个部分
然后在把right 作为左边 跟 left 作为右边 合起来
看看是不是与B相等
原理就是 如果A B  在A中找到了与B 第一个字符 相等的字符后 如果是B是A的旋转的话
那么 我们就把 相等字符右边 旋转到左边 去检查
'''