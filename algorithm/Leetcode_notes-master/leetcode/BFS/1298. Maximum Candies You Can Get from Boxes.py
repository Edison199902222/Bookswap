class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        queue = collections.deque()
        visited = set()
        cur_key = set()
        cur_box = set()
        result = 0
        for i in initialBoxes:
            if status[i] == 1:
                queue.append(i)
                visited.add(i)
            cur_box.add(i)

        while queue:
            cur_node = queue.popleft()
            result += candies[cur_node]
            # 每次检查 当前可以打开的key 和 box 是否真的可以打开
            # 可以打开有两个条件，一个是有key 或者本来就是开着， 一个是box 被我们找到了
            for key in keys[cur_node]:
                cur_key.add(key)
                if key in cur_box and key not in visited:
                    queue.append(key)
                    visited.add(key)
            for box in containedBoxes[cur_node]:
                cur_box.add(box)
                if box in cur_box and box not in visited and (box in cur_key or status[box] == 1):
                    queue.append(box)
                    visited.add(box)
        return result