class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.queue = deque()
        for v in [v1, v2]:  # For the follow up question, simply just all the array here like v1, v2,...vk
            if v:
                self.queue.append((v, 0))

    def next(self):
        """
        :rtype: int
        """
        cur_val, cur_pos = self.queue.popleft()
        if cur_pos < len(cur_val):
            val = cur_val[cur_pos]
            self.queue.append((cur_val, cur_pos + 1))
            return val
    '''
    每次得到 queue最左边的一个
    然后检查当前要pop的index 是否超过当前list的最大index
    如果不超过 那么我们就把对应的index pop出 并且把当前list 的pos 加上1 进行下一轮
    '''
    def hasNext(self):
        """
        :rtype: bool
        """
        # 每次如果queue的第一个 index 是合法，那么直接return true
        # 如果不合法，那么popleft 并且找到下一个合法的v
        cur_queue = self.queue
        flag = False
        while cur_queue:
            cur_val, cur_pos = cur_queue[0]
            if cur_val and cur_pos < len(cur_val):
                flag = True
                return flag
            else:
                flag = False
                self.queue.popleft()
        return flag
    '''
    hasnext 是判断 整个queue 是否合法
    那么我们遍历 整个queue
    对于每个小queue来说  我们看看是否pos 超过当前小queue的index了
    如果超过了 我们就把当前小queue pop出去
    然后继续循环
    只要有一个小queue 没有超过 我们就可以reutnr true
    '''


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.index1 = 0
        self.index2 = 0
        self.next_item = None
        self.flag = True

    def next(self) -> int:
        self.hasNext()
        temp, self.next_item = self.next_item, None
        return temp

    def hasNext(self) -> bool:
        if self.next_item != None:
            return True
        if self.flag:
            if self.index1 < len(self.v1):
                self.next_item = self.v1[self.index1]
                self.index1 += 1
                self.flag = False
                return True
            elif self.index2 < len(self.v2):
                self.next_item = self.v2[self.index2]
                self.index2 += 1
                self.flag = False
                return True
            else:
                return False
        elif not self.flag:
            if self.index2 < len(self.v2):
                self.next_item = self.v2[self.index2]
                self.index2 += 1
                self.flag = True
                return True
            elif self.index1 < len(self.v1):
                self.next_item = self.v1[self.index1]
                self.index1 += 1
                self.flag = True
                return True
            else:
                return False
        return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())