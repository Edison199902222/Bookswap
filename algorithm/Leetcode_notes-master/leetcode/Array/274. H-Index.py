
'''
二分法
题目说：我们需要找到一个h，数组中所有的数， 至少有 h 个 大于等于 h

'''


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations.sort()
        left = 0
        n = len(citations)
        right = citations[n - 1]
        while left + 1 < right:
            mid = (left + right) // 2
            if self.decide(mid, citations):
                left = mid
            else:
                right = mid

        if self.decide(right, citations):
            return right
        if self.decide(left, citations):
            return left
        return 0

    def decide(self, H, citations):
        count = 0
        for i in citations:
            if i >= H:
                count += 1
        return count >= H

    class Solution:
        def hIndex(self, citations: List[int]) -> int:
            # 用数组 统计 h-index 为 index 的数量
            n = len(citations)
            counter = [0] * (n + 1)
            for i in range(len(citations)):
                # 大于length 的话，看作是length h-index
                counter[min(n, citations[i])] += 1

            sums = 0
            result = 0
            # 从后往前，sums 算的是当前大于等于 h-index i 文章的数量
            # 一旦文章数量大于等于 h-index 了，找到目标了
            for i in range(len(counter) - 1, - 1, -1):
                sums += counter[i]
                if sums >= i:
                    result = i
                    break
            return result

    class Solution:
        def hIndex(self, citations: List[int]) -> int:
            citations.sort(reverse=True)
            h_index = 0
            # 从大到小，加h-index
            for i in range(len(citations)):
                if citations[i] >= h_index:
                    h_index += 1
            return h_index
if __name__ =="__main__":
    solution = Solution()
    print(solution.hIndex([3,0,6,1,5]))