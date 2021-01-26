class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        # 只需要看最后停在哪里就行了，以停在哪个点进行bfs
        # 这道题，每次放进queue 中的 点 都是从任意方向撞过来，并且触碰到墙后，触碰墙之前的最后一个节点
        queue = collections.deque()
        queue.append((start[0], start[1]))
        visited = set()
        visited.add((start[0], start[1]))
        m = len(maze)
        n = len(maze[0])
        while queue:
            x, y = queue.popleft()
            # 因为都是合法并且触碰到墙之前的一个节点，所以检查就行了
            if x == destination[0] and y == destination[1]:
                return True
            for dirc in [(1, 0), (- 1, 0), (0, 1), (0, -1)]:
                row = x + dirc[0]
                col = y + dirc[1]
                # 每次沿着方向一直走，直到碰到墙
                while 0 <= row < m and 0 <= col < n and maze[row][col] == 0:
                    row += dirc[0]
                    col += dirc[1]
                # 现在的点是碰到墙时候的点，还需要back 一次
                row -= dirc[0]
                col -= dirc[1]
                # 检查这个点是不是没有visited 过
                if (row, col) not in visited:
                    queue.append((row, col))
                    visited.add((row, col))
        return False
