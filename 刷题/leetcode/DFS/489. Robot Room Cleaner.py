# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.dfs(robot, 0, 0, set(), 0)

    def dfs(self, robot, i, j, visited, direction):
        robot.clean()
        visited.add((i, j))
        for index in range(4):
            # 当前的方向 去尝试下面四个方向
            x, y = self.dir[(direction + index) % 4]
            # 得到新的坐标
            new_x, new_y = i + x, j + y
            # 检查是否去过，已经是否可以去
            if (new_x, new_y) not in visited and robot.move():
                # 进入下一层递归
                self.dfs(robot, new_x, new_y, visited, (direction + index) % 4)
                # 回溯，回来，然后方向变成初始化的方向
                robot.turnRight()
                robot.turnRight()
                # 把方向转成逆序，然后回来
                robot.move()
                # 把方向调回去之前的方向
                robot.turnLeft()
                robot.turnLeft()
            # 跟着direction，下一轮要更新新的方向
            robot.turnRight()
        return
