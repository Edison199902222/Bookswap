class Solution(object):
    def minPushBox(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        # 确定 target， box， people 的位置
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "T":
                    target_i, target_j = i, j
                elif grid[i][j] == "S":
                    people_i, people_j = i, j
                elif grid[i][j] == "B":
                    box_i, box_j = i, j

        seen = set()
        # 用 人 和 box 的位置作为访问过的节点，因为第二次如果访问相同状态的节点，那么肯定是不好的，因为cost 一定比第一次高
        seen.add((people_i, people_j, box_i, box_j))
        heap = []
        # 由cost， people的位置 和 box 的位置 组合成的tuple 作为我们的状态
        heapq.heappush(heap, (0, people_i, people_j, box_i, box_j))
        while heap:
            cost, p_i, p_j, b_i, b_j = heapq.heappop(heap)
            if b_i == target_i and b_j == target_j:
                return cost
            for d_i, d_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = p_i + d_i, p_j + d_j
                new_bi, new_bj = b_i + d_i, b_j + d_j
                if new_x < 0 or new_y < 0 or new_x >= m or new_y >= n:
                    continue
                if new_x == b_i and new_y == b_j and 0 <= new_bi < m and 0 <= new_bj <= n and grid[new_x][
                    new_y] != "#" and (new_x, new_y, new_bi, new_bj) not in seen:
                    heapq.heappush(heap, (cost + 1, new_x, new_y, new_bi, new_bj))
                    seen.add((new_x, new_y, new_bi, new_bj))
                elif grid[new_x][new_y] != "#" and (new_x, new_y, b_i, b_j) not in seen:
                    heapq.heappush(heap, (cost, new_x, new_y, b_i, b_j))
                    seen.add((new_x, new_y, b_i, b_j))
        return - 1