'''
只需要先排序
然后跟排序对的list 进行对比
错了的 count+1 就可以
'''

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        count = 0
        compared_list = sorted(heights)
        for i in range(len(heights)):
            if compared_list[i] != heights[i]:
                count += 1
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.heightChecker([1,1,4,2,1,3]))