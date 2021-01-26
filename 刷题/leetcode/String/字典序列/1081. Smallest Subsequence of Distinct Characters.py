class Solution:
    def smallestSubsequence(self, text: str) -> str:
        result = []
        counter = collections.Counter(text)
        for i in range(len(text)):
            if text[i] not in result:
                while result and text[i] < result[-1] and counter[result[-1]] > 0:
                    result.pop()
                result.append(text[i])
            counter[text[i]] -= 1
        return "".join(result)