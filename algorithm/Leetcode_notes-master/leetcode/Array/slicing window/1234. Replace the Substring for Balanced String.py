class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = collections.Counter(s)
        times = len(s) // 4
        delete = collections.Counter()
        for i in counter:
            if counter[i] > times:
                delete[i] = counter[i] - times
        left = 0
        result = float("inf")
        delete_total = len(delete)
        if delete_total == 0:
            return 0
        for right in range(len(s)):
            if s[right] not in delete:
                continue
            delete[s[right]] -= 1
            if delete[s[right]] == 0:
                delete_total -= 1
            while delete_total == 0:
                result = min(result, right - left + 1)
                if s[left] not in delete:
                    left += 1
                    continue
                delete[s[left]] += 1
                if delete[s[left]] == 1:
                    delete_total += 1
                left += 1
        return result
