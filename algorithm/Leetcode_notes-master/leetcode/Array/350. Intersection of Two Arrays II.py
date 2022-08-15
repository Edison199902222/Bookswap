'''
和349 不一样的是 只要一样的 我们就要添加进result中
我们建立一个字典
把短的那个列表 中每个元素出现的次数找出来
然后遍历第二个列表 发现这个元素如果在字典中的次数大于0 那么就添加进result中 并且字典的计数数字 - 1
'''
import collections
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.intersect(nums2,nums1)
        num1_dic = collections.defaultdict(int)
        result = []
        for i in nums1:
            num1_dic[i] += 1
        for i in range(len(nums2)):
            if num1_dic[nums2[i]] > 0:
                result.append(nums2[i])
                num1_dic[nums2[i]] -= 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.intersect([1,2,2,1],[2,2,1]))