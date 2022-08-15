class Solution(object):
    def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str
        """
        S_old = S
        left = 0
        right = len(S)
        # 算出编码
        S = [ord(S[i]) - ord("a") for i in range(len(S))]
        n = len(S)
        module = 2 ** 32
        while left + 1 < right:
            mid = (left + right) // 2
            if self.caculate(S, mid, n, module) != -1:
                left = mid
            else:
                right = mid
        start = self.caculate(S, right, n, module)
        if start != -1:
            return S_old[start: start + right]
        start = self.caculate(S, left, n, module)
        if start != -1:
            return S_old[start: start + left]
        return ""

    def caculate(self, S, mid, n, module, base=26):
        if mid < 1:
            return -1
        code_s = 0
        # 算出第一个string 的编码和
        for i in range(mid):
            code_s = (code_s * base + S[i]) % module
        dic = {code_s}
        #
        aL = (base ** mid) % module
        for left in range(1, n - mid + 1):
            # 每次添加一个新的， 就要把前面一个的值减去
            # 每添加一个值，新的值不乘base， 因为整体都乘了base， 要减去的值需要减掉base * 长度
            code_s = (code_s * base - S[left - 1] * aL + S[left + mid - 1]) % module
            if code_s in dic:
                return left
            dic.add(code_s)
        return - 1


class Solution(object):
    def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str
        """
        S_old = S
        left = 0
        right = len(S)
        # 算出编码
        S = [ord(S[i]) - ord("a") for i in range(len(S))]
        n = len(S)
        while left + 1 < right:
            mid = (left + right) // 2
            if self.caculate(S, mid, n, ) != -1:
                left = mid
            else:
                right = mid
        start = self.caculate(S, right, n, )
        if start != -1:
            return S_old[start: start + right]
        start = self.caculate(S, left, n)
        if start != -1:
            return S_old[start: start + left]
        return ""

    def caculate(self, S, mid, n, base=26):
        # 取两个 module， 避免冲突
        module1 = 10 ** 9 + 7
        module2 = 10 ** 9 + 9
        code_s1 = code_s2 = 0
        # 用两个hash 作为 标示，避免冲突
        # 算第一个string的值
        for i in range(mid):
            code_s1 = (code_s1 * base + S[i]) % module1
            code_s2 = (code_s2 * base + S[i]) % module2
        # 算出total base
        total_base1 = (base ** mid) % module1
        total_base2 = (base ** mid) % module2
        # 如果出现和set中一样的值，说明出现两次
        check = set()
        check.add((code_s1, code_s2))
        for i in range(1, n - mid + 1):
            code_s1 = (code_s1 * base - S[i - 1] * total_base1 + S[i + mid - 1]) % module1
            code_s2 = (code_s2 * base - S[i - 1] * total_base2 + S[i + mid - 1]) % module2
            if (code_s1, code_s2) in check:
                return i
            check.add((code_s1, code_s2))
        return -1

