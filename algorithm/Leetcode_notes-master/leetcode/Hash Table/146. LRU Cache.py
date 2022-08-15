'''
用一个 hash table 加上一个链表来实现
hash table 中储存的是给出的 要储存的 key 跟 对应 key 在链表中的node 的前一个 node
然后 最常用的node 会放到链表的尾部
如果 链表长度超过了最大数量的话 会把头给pop出去 因为头部的 node是最不常用的

'''


class LinkNode(object):
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = {}
        self.dummy = LinkNode()
        self.tail = self.dummy
        self.capacity = capacity

    def pop_front(self):
        head = self.dummy.next
        del self.dic[head.key]
        self.dummy.next = head.next
        self.dic[head.next.key] = self.dummy

    def kick(self, prev):
        node = prev.next
        if node == self.tail:
            return
        prev.next = node.next
        self.dic[prev.next.key] = prev
        node.next = None
        self.push_back(node)

    def push_back(self, node):
        self.dic[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return - 1
        prev = self.dic[key]
        current = prev.next
        self.kick(prev)
        return current.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        if key in self.dic:
            self.kick(self.dic[key])
            self.dic[key].next.value = value
            return
        self.push_back(LinkNode(key, value))
        if len(self.dic) > self.capacity:
            self.pop_front()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class Node(object):
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dummy = Node()
        self.tail = self.dummy
        self.capacity = capacity
        self.dic = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return - 1
        temp_node = self.dic[key]
        if self.tail == temp_node:
            return temp_node.val
        self.kick(temp_node)
        return temp_node.val

    def kick(self, node):
        if node == self.tail:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        self.insert_tail(node)

    def insert_tail(self, node):
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def pop_head(self):
        cur = self.dummy.next
        del self.dic[cur.key]
        self.dummy.next = cur.next
        cur.next.prev = self.dummy
        cur.next = None

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            node = self.dic[key]
            self.kick(node)
            node.val = value
        else:
            node = Node(key, value)
            self.dic[key] = node
            self.insert_tail(node)
        if len(self.dic) > self.capacity:
            self.pop_head()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)