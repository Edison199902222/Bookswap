class Solution(object):
    def maxSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i, j, n, m = 0, 0, len(nums1), len(nums2)
        a, b, result, mod = 0, 0, 0, 10 ** 9 + 7
        # 双指针
        # a表示 在nums1 遇到 和 nums2相同的数前的总和
        # b表示 在nums2 遇到 和 nums1相同的数前的总和
        while i < n or j < m:
            # 尽量让两个指针指向的数 靠近
            # 因为是sort的，所以每次选走较小的那个，让较小的靠近较大的
            if i < n and (j == m or nums1[i] < nums2[j]):
                a += nums1[i]
                i += 1
            elif j < m and (i == n or nums2[j] < nums1[i]):
                b += nums2[j]
                j += 1
            # 如果发现一样的话，两条path 取最大值
            else:
                result += max(a, b) + nums2[j]
                i += 1
                j += 1
                a = 0
                b = 0
        return (result + max(a, b)) % mod

