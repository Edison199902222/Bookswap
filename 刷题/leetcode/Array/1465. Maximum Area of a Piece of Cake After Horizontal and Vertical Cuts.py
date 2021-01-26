class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        h_max = float("-inf")
        v_max = float("-inf")
        horizontalCuts = [0] + sorted(horizontalCuts) + [h]
        verticalCuts = [0] + sorted(verticalCuts) + [w]
        for i in range(len(horizontalCuts) - 1):
            h_max = max(h_max, horizontalCuts[i + 1] - horizontalCuts[i])
        for i in range(len(verticalCuts) - 1):
            v_max = max(v_max, verticalCuts[i + 1] - verticalCuts[i])
        return (h_max * v_max) % (10 ** 9 + 7)

