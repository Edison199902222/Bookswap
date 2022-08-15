class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        record = [float("inf") for i in range(n)]
        record[src] = 0
        K = min(K, n - 2)
        for i in range(K + 1):
            cur = record.copy()
            # 因为限制了步数，cur 代表这一层要走的，只能由上一层record 转移来
            # 不能由当前层转移来，不然步数会走很多
            for x, y, cost in flights:
                cur[y] = min(cur[y], record[x] + cost)
            record = cur.copy()
            print(record)
        return record[dst] if record[dst] != float("inf") else -1