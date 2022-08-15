class ThroneInheritance:

    def __init__(self, kingName: str):
        self.dic = collections.defaultdict(list)
        self.root = kingName
        self.dead_list = set()

    # 建立图， 每个父亲对应下面的孩子节点
    def birth(self, parentName: str, childName: str) -> None:
        self.dic[parentName].append(childName)

    # 死去的人 加入 set
    def death(self, name: str) -> None:
        self.dead_list.add(name)

    # dfs， 因为名字不会重复，并且一直走下去，是单向图，树的结构，不会有回头路的情况
    # 很像中序遍历
    def getInheritanceOrder(self) -> List[str]:
        result = []
        self.dfs(self.root, result)
        return result

    def dfs(self, cur, result):
        if cur not in self.dead_list:
            result.append(cur)
        for neighbor in self.dic[cur]:
            self.dfs(neighbor, result)
        return

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()