class Solution:
    def longestAwesome(self, s: str) -> int:
        # 特殊情况，当前前缀数组可以直接变换成回文串
        prefix = {0: -1}
        result = 0
        cur = 0
        # 数字只有 0 ～ 9，所以用bit 表示状态，比如 有一个2出现，bit表示出来就是 100
        # 1 表示出现了奇数次，0表示出现了偶数次
        # awesome substring 意思是 只要一段字符串内 所有字符只允许一个出现奇数次，其他都要出现偶数次
        # 用cur 去truck 当目前为止的string 各个字符出现次数的状态
        for i in range(len(s))：
        cur ^= (1 << int(s[i]))
        # 因为数字只有 0 ～ 9， 尝试与0-9进行异或后再查看，考虑到奇数长度的回文串
        # 尝试把每一个 奇数位的1，变成0，如果只拥有一位奇数的话，temp会变成0
        for j in range(10):
            temp = cur ^ (1 << j)
            # 如果temp在之前出现了，那么当前的i - temp出现的index，这样就全是偶数了
            if temp in prefix:
                result = max(result, i - prefix[temp])
        # 如果之前有相同的cur 出现的话， 那么用整个字符串去掉 前面的， 后半部分就全是偶数次出现的
        # 与之前的某一个前缀数组相等，后面这一段可以是awesome string
        if cur in prefix:
            result = max(result, i - prefix[cur])
        else:
            prefix[cur] = i

    return result
