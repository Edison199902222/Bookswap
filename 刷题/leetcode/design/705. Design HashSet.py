class Node(object):
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Bucket(object):
    def __init__(self):
        self.dummy = Node(0)

    # 检查key 在不在当前链表中
    def check(self, key):
        cur = self.dummy.next
        while cur is not None:
            if cur.val == key:
                return True
            cur = cur.next
        return False

    # 插入一个新的value 作为头
    def insert(self, key):
        # 如果key不存在当前链表的话
        if not self.check(key):
            node = Node(key)
            node.next = self.dummy.next
            self.dummy.next = node
        return

    def pop(self, key):
        prev = self.dummy
        cur = prev.next
        while cur is not None:
            if cur.val == key:
                prev.next = cur.next
                cur.next = None
                return
            prev = cur
            cur = cur.next
        return


class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.range = 769
        self.bucketArray = [Bucket() for i in range(self.range)]

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self.get_index(key)
        self.bucketArray[index].insert(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self.get_index(key)
        self.bucketArray[index].pop(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        index = self.get_index(key)
        return self.bucketArray[index].check(key)

    def get_index(self, key):
        return key % self.range


class Node:
    def __init__(self, key=None):
        self.k = key
        self.next = None


# 跟 706 一样的思路
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = [None for i in range(10001)]

    def get_index(self, key):
        return key % 10001

    def find(self, node, key):
        prev = None
        while node != None and node.k != key:
            prev = node
            node = node.next
        return prev

    def add(self, key: int) -> None:
        index = self.get_index(key)
        node = self.hashset[index]
        if node == None:
            self.hashset[index] = Node()
        prev = self.find(self.hashset[index], key)
        if prev.next == None:
            prev.next = Node(key)
        else:
            return

    def remove(self, key: int) -> None:
        index = self.get_index(key)
        node = self.hashset[index]
        if node == None:
            return
        prev = self.find(node, key)
        if prev.next == None:
            return
        prev.next = prev.next.next

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = self.get_index(key)
        node = self.hashset[index]
        if node == None:
            return False
        prev = self.find(node, key)
        if prev.next == None:
            return False
        return True

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)