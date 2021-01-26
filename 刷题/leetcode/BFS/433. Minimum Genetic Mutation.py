import collections


class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bank = set(bank)
        queue = collections.deque([[start, 0]])
        while queue:
            node, cost = queue.popleft()
            if node == end:
                return cost
            for c in "ACGT":
                for i in range(len(node)):
                    new_node = node[:i] + c + node[i + 1:]
                    if new_node in bank:
                        queue.append([new_node, cost + 1])
                        bank.remove(new_node)
        return - 1
'''
与127 题基本一样
'''