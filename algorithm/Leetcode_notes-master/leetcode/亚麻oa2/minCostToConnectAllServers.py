

def minCostToConnectAllServers(nums, arr):
    mincost = []
    visited = set()
    arr = sorted(arr, key = lambda x : x.cost)
    for city in arr:
        A = city.firstTown
        B = city.secondTown
        visited.add(A)
        visited.add(B)
        mincost.append(city)
        if len(visited) >= nums:
            return mincost
    return mincost