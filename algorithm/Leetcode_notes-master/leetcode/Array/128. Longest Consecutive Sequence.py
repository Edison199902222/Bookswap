'''
我们用字典
遍历这个数组 如果这个数字 不存在字典之中的话
那么我们就 把比它小一位的数字作为left
比它大一位的数字 作为right
我们在字典中找 是否lefrt 跟 right 已经出现在字典中 并且得到它的value 值
key ： value 这里的意思是
key作为每一个数字 value意思是 作为key 存在的最大连续的个数
比如4 ： 2 意思是 4 已经有两个连续的数字了 所以当我们找到3 时
那么 我们会寻找它的right有几个连续的序列 right是 4 那么 3的连续序列 就会等于 他的左边2 的连续序列加上 右边 4的连续序列数量 再加上自己 也就是+1
并且 还需要更新 字典里 作为自己的最长序列数量
还要更新 由当前数字 减去 left 或者 right 的数字的最大连续序列
为什么需要更新左边跟右边呢 因为如果不更新的话 例如【1，2，0，1】 当遇到0的时候 要把right 也就是 1的次数加起来 但是这时候1 并没有更新 所有return会是2
'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # key : value, key = 数组的值，value = 对应 Longest Consecutive Sequence
        dic = {}
        result = 0
        for num in nums:
            # 出现第一次时， 计算
            if num not in dic:
                # 比自己小1 的 Longest Consecutive Sequence
                left = dic.get(num - 1, 0)
                # 比自己大1 的 Longest Consecutive Sequence
                right = dic.get(num + 1, 0)
                # 加一起就是当前的Longest Consecutive Sequence
                total = left + 1 + right
                result = max(result, total)
                # 重复赋值给left，right, num,
                # 因为在left ～ right 中的数不会重复计算第二遍，要更新的数字只能是left 之前的数字，跟right之后的数
                # 所以left right num 都需要更新成total
                dic[num] = total
                dic[num + right] = total
                dic[num - left] = total
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([4,1,3,2,]))
