class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> \
    List[str]:
        graph = collections.defaultdict(list)
        for i in range(len(friends)):
            for j in friends[i]:
                graph[i].append(j)
                graph[j].append(i)

        final_node = []
        queue = collections.deque()
        queue.append(id)
        visited = set()
        visited.add(id)
        level += 1
        while level > 0:
            level -= 1
            cur = []
            for i in range(len(queue)):
                node = queue.popleft()
                for j in watchedVideos[node]:
                    cur.append(j)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
            final_node = cur
        counter = collections.Counter(final_node)
        counter = sorted(counter, key=lambda x: (counter[x], x))
        return [x for x in counter]


