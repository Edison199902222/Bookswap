class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """

    def sortLetters(self, chars):
        self.quick_sort(chars, 0, len(chars) - 1)

    def quick_sort(self, chars, left, right):
        if left < right:
            pos = self.partition(chars, left, right)
            self.quick_sort(chars, left, pos - 1)
            self.quick_sort(chars, pos + 1, right)

    def partition(self, chars, left, right):
        piviot = chars[right]
        i = left
        for j in range(left, right):
            if ord(chars[j]) > ord(piviot):
                chars[j], chars[i] = chars[i], chars[j]
                i += 1
        chars[i], chars[right] = chars[right], chars[i]
        return i
'''
变相考察quick sort
'''