class Solution:
    def lastSubstring(self, s: str) -> str:
        # 因为字典顺序，可以看出 ab abc 两个字符中， abc 更大，因为两个字符相同时，谁更长谁order 更大
        # 所以，可以确定我们只需要找到 最大substring 的起始点，然后把前面都切掉，后缀就是答案
        # 利用双指针来找起始点
        # i j 两个指针 指向数组的两个字符，维持 i +k ， j +k 两个substring
        # 每次比较，如果i 的更大，那么j就要更新到j + k + 1， 因为在j ～ j + k 之间的字符都是小于i的，不然也不会等到现在更新
        # 如果 j更大，那么用j的去更新i，j移动到自己下一个位置 找最大string，继续去比较
        i = 0
        j = 1
        k = 0
        while j + k < len(s):
            # 等于的情况，k继续增加，这时 i j substring 相等
            if s[i + k] == s[j + k]:
                k += 1
                continue
            # 如果， i 的substirng 大于 j，那么j 继续找下一个
            elif s[i + k] > s[j + k]:
                j = j + k + 1
            # i 小于 j， 更新掉i， j 移动一个位置
            else:
                i = j
                j = i + 1
            # 到这里证明i 或者j 都更新了，所以要重设k = 0
            k = 0
        return s[i:]

