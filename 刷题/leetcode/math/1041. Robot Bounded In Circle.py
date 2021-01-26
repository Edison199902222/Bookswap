class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        # 初始化方向， 向北
        dx, dy = 0, 1
        # 点，初始化
        x, y = 0, 0
        for i in range(len(instructions)):
            if instructions[i] == "G":
                x += dx
                y += dy
            # 向左旋转， 点的变化
            elif instructions[i] == "L":
                dx, dy = -dy, dx
            # 向右旋转， 点的变化
            else:
                dx, dy = dy, -dx
        # 如果转一圈就回到原点，自然是true
        # 如果题目中的指令结束之后，机器人不在原点，那么说明它相对原点移动了一个向量v。
        #机器人在指令结束后的位置成为了新的原点，题目说机器人的初始状态时是面向北的，
        # 那么如果在新的原点上仍然面向北，那么一定还会继续向第一次一样相对新的原点移动相同的向量v，此时机器人距原点的向量是2v。
        if (x == 0 and y == 0) or (dx, dy) != (0, 1):
            return True
        return False