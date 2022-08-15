class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        # 前后扫
        n = len(seats)
        left = [float("inf") for i in range(n)]
        prev = -1
        for i in range(len(seats)):
            if seats[i] == 1:
                prev = i
                left[i] = 0
            else:
                if prev != -1:
                    left[i] = i - prev

        prev = -1
        for i in range(n - 1, -1, -1):
            if seats[i] == 1:
                prev = i
            else:
                if prev != - 1:
                    left[i] = min(left[i], prev - i)
        result = 0
        for i in range(n):
            if left[i] != float("inf"):
                result = max(result, left[i])
        return result


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # 记录第一个1的位置
        left = -1
        # 连续遇到了几个0
        count = 0
        result = 0
        for i in range(len(seats)):
            if seats[i] == 0:
                count += 1
            else:
                if left < 0:
                    # 因为左边没有1，所以最大距离就是count
                    distance = count
                # 左边有1
                else:
                    # 10001, 中间有奇数个0，3 个0，左右都有1，那么距离就是中点，但因为奇数，所以需要加1才是距离
                    distance = count // 2 + count % 2
                left = i
                count = 0
                result = max(result, distance)
        # 最后有可能一连串都是0，[1,0,0,0]
        return max(result, count)
