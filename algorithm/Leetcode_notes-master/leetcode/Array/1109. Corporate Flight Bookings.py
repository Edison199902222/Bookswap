'''
其实可以堪称上车问题
【i，j,k]
k个人从i站上车 j站下车
最后其实只要每个加前面的就好

'''
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*n
        for start, end, seat in bookings:
            res[start-1]+=seat
            if end < n:
                res[end]-=seat
        for i in range(1,n):
            res[i]+=res[i-1]
        return res