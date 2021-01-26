class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == newColor:
            return image
        self.direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        return self.dfs(sr, sc, image, image[sr][sc], newColor)

    def dfs(self, row, col, image, oldcolor, newcolor):
        if row >= len(image) or row < 0 or col >= len(image[0]) or col < 0 or image[row][col] != oldcolor:
            return
        image[row][col] = newcolor
        for i in self.direction:
            self.dfs(row + i[0], col + i[1], image, oldcolor, newcolor)
        return image
'''
有点像染色问题
'''