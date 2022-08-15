class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        # queue 中最后一个元素就是头
        self.queue = collections.deque()
        self.queue.append([0, 0])
        # food 变成deque， 方便popleft
        self.food = collections.deque(food)
        self.dir = {"U": [-1, 0], "D": [1, 0], "R": [0, 1], "L": [0, -1]}
        self.w = width
        self.h = height

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """
        new_head = [self.queue[-1][0] + self.dir[direction][0], self.queue[-1][1] + self.dir[direction][1]]
        # 贪吃蛇可以移动到尾巴部分，不算犯规
        if (new_head in self.queue and new_head != self.queue[0]) or new_head[0] < 0 or new_head[0] >= self.h or \
                new_head[1] < 0 or new_head[1] >= self.w:
            return - 1
        # 核心思想就是，当遇到 food 的时候，直接把food的点 作为头 添加到 蛇 的所有位置中
        # 如果没有遇到food，把 新节点 append 到蛇的所有位置之后，再pop掉尾巴
        if self.food and new_head == self.food[0]:
            self.queue.append(new_head)
            self.food.popleft()
        else:
            self.queue.append(new_head)
            self.queue.popleft()
        return len(self.queue) - 1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)