class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        queue = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue = []
                    queue.append((i + 1, j, 1))
                    queue.append((i - 1, j, 1))
                    queue.append((i, j + 1, 1))
                    queue.append((i, j - 1, 1))
                while queue:
                    row, col, val = queue.pop(0)
                    if row < 0 or row >= len(rooms) or col < 0 or col >= len(rooms[0]) or rooms[row][col] <= val:
                        continue
                    rooms[row][col] = val
                    queue.append((row + 1, col, val + 1))
                    queue.append((row - 1, col, val + 1))
                    queue.append((row, col + 1, val + 1))
                    queue.append((row, col - 1, val + 1))
        return rooms
'''
使用bfs 遇到gate 我们就开始搜索 其他的空房间离当前gate有多远
我们每次 遇到gate 也就是0 我们开始
把上下左右 放进quenue里面 放进去的是坐标 跟离当前gate 有多远
然后用while bfs 搜索 其他empty room 上下左右 
'''


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue = collections.deque([[i, j, 0]])
                    while queue:
                        x, y, distance = queue.popleft()
                        if 0 <= x < len(rooms) and 0 <= y < len(rooms[0]) and rooms[x][y] >= distance:
                            rooms[x][y] = distance
                            queue.append([x + 1, y, distance + 1])
                            queue.append([x - 1, y, distance + 1])
                            queue.append([x, y + 1, distance + 1])
                            queue.append([x, y - 1, distance + 1])
        return rooms

