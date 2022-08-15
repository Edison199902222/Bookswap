class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 用bitset
        memo = {0: -1}
        # 分配给五个元素， bit 的位置
        # 出现a 的话 会变成00001， e的话00010
        dic = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
        result = 0
        cur = 0
        for index, char in enumerate(s):
            if char in dic:
                # 记录当前位，进行异或
                # 如果当前0 到 index 中，当前char 是偶数个，异或后是0
                # 如果是奇数个，异或后是1
                cur ^= (1 << dic[char])
            # cur 其实是前缀和，把每一组字符变成相应的00000五个bit组成的前缀和，来记录每个vowel的情况
            # 如果当前前缀和之前没有出现过，那么记录下来 因为只要有偶数就会变成全0，如果有一个不为0并且之前没有出现，
            # 说明当前cur 的array中，没有一段是全是偶数的
            if cur not in memo:
                memo[cur] = index
            # 如果之前出现过的话，说明之前的subarray有一段跟现在含有的是相同，所以把subarray减去，中间的就是全是偶数的情况
            else:
                result = max(result, index - memo[cur])
        return result
