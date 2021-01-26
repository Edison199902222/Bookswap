class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        # dijk
        # time:m*n*log(mn)
        heap = []
        heapq.heappush(heap, (0, start[0], start[1]))
        visited = collections.defaultdict(int)
        visited[(start[0], start[1])] = 0
        while heap:
            step, x, y = heapq.heappop(heap)
            if x == destination[0] and y == destination[1]:
                return step
            for dir_x, dir_y in [(1, 0), (-1, 0), (0, 1), (0, - 1)]:
                new_x = x
                new_y = y
                new_step = step
                while 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] == 0:
                    new_x += dir_x
                    new_y += dir_y
                    new_step += 1
                new_x -= dir_x
                new_y -= dir_y
                new_step -= 1
                if (new_x, new_y) not in visited or visited[(new_x, new_y)] > new_step:
                    visited[(new_x, new_y)] = new_step
                    heapq.heappush(heap, (new_step, new_x, new_y))
        return -1