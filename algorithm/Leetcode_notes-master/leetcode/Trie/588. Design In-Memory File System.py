class Node:
    def __init__(self):
        self.child = collections.defaultdict(Node)
        self.context = ""


class FileSystem:

    def __init__(self):
        self.root = Node()

    def find(self, path):
        cur = self.root
        if len(path) == 1:
            return cur
        # 第一个如果是/，会变空格，所以要去掉第一个
        for word in path.split("/")[1:]:
            cur = cur.child[word]
        return cur

    def ls(self, path: str) -> List[str]:
        cur = self.find(path)
        # 如果是file的话，return file name
        if cur.context:
            return [path.split("/")[-1]]
        return sorted(cur.child.keys())

    def mkdir(self, path: str) -> None:
        cur = self.find(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.find(filePath)
        cur.context += content

    def readContentFromFile(self, filePath: str) -> str:
        cur = self.find(filePath)
        return cur.context

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)