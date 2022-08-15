# uf 第二种模版
class UnionFind(object):
    def __init__(self):
        self.father = {}
        self.count = 0

    def union(self, a, b):
        father_a = self.find(a)
        father_b = self.find(b)
        if father_a != father_b:
            self.father[father_b] = father_a
            self.count -= 1

    def find(self, child):
        if self.father[child] == child:
            return child
        # 路径压缩，不用全部往上找
        self.father[child] = self.find(self.father[child])
        return self.father[child]


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # 记录岛屿的坐标
        island = set()
        result = []
        uf = UnionFind()
        for x, y in positions:
            # 如果 x y 已经遍历过并且是岛屿， 直接添加现在的count
            if (x, y) in island:
                result.append(uf.count)
                continue
            # 把新的岛屿 放进uf中
            uf.father[(x, y)] = (x, y)
            # count 加上1
            uf.count += 1
            # 四个方向，看有没有连在一起的岛屿
            for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if (new_x, new_y) in island:
                    uf.union((x, y), (new_x, new_y))
            # 把新的岛屿放进 岛屿坐标中
            island.add((x, y))
            # 添加此刻岛屿数量
            result.append(uf.count)
        return result