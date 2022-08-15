class Node:
    def __init__(self, k=None, v=None):
        self.k = k
        self.v = v
        self.next = None


# 链表来实现
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 取一个prime number 防止哈希碰撞 hash collisions
        # 表上的第一个node 是头 后面的才是我们要储存的东西 拉链一样
        self.hashmap = [None for i in range(10001)]

    def index(self, key):
        return key % 10001

    # 找到目标节点 的前一个
    def find(self, node, key):
        prev = None
        while node != None and node.k != key:
            prev = node
            node = node.next
        return prev

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        # 先从index 定位 要寻找的拉链
        index = self.index(key)
        # 定位头
        node = self.hashmap[index]
        # 如果头是none， 说明还未有node 插入过
        if node == None:
            self.hashmap[index] = Node()
        # 根据头，找key 对应的node 的前一个
        prev = self.find(self.hashmap[index], key)
        # 如果key 对应的node 是none， 说明没有插入过
        # 生成一个 node  插进去
        if prev.next == None:
            prev.next = Node(key, value)
        # 如果node 以及存在，更新value
        else:
            prev.next.v = value
        return

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = self.index(key)
        node = self.hashmap[index]
        # 要检查node 是否是none， 因为有可能不存在
        if node == None:
            return - 1
        prev = self.find(node, key)
        if prev.next == None:
            return - 1
        return prev.next.v

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = self.index(key)
        node = self.hashmap[index]
        if node == None:
            return - 1
        prev = self.find(node, key)
        if prev.next == None:
            return - 1
        prev.next = prev.next.next
        return

    # Your MyHashMap object will be instantiated and called as such:


# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
'''
利用链表 来实现 hash map
hash map原理是 把本来需要用m 个 来表示的东西 压缩到n个 
比如这道题
我们创建了 长度 为10001 的数组
然后 每次 把key 给 取余
这样就找到了 这个key 大概会储存在哪 
然后再取找 这个key 大概在哪的节点 再用 链表取找 key实际上储存在链表的哪个位置
数组中每个 idnex 其实表示的是 链表的头
'''
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)