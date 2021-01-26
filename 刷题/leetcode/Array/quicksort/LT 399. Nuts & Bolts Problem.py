"""
class Comparator:
    def cmp(self, a, b)
You can use Compare.cmp(a, b) to compare nuts "a" and bolts "b",
if "a" is bigger than "b", it will return 1, else if they are equal,
it will return 0, else if "a" is smaller than "b", it will return -1.
When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
"""


class Solution:
    # @param nuts: a list of integers
    # @param bolts: a list of integers
    # @param compare: a instance of Comparator
    # @return: nothing
    def sortNutsAndBolts(self, nuts, bolts, compare):
        # write your code here
        self.quicksort(nuts, bolts, 0, len(nuts) - 1, compare.cmp)

    def quicksort(self, nuts, bolts, left, right, cmp):
        if left < right:
            pos = self.partition(bolts, left, right, nuts[(left + right) // 2], cmp)
            self.partition(nuts, left, right, bolts[pos], cmp)
            self.quicksort(nuts, bolts, left, pos - 1, cmp)
            self.quicksort(nuts, bolts, pos + 1, right, cmp)

    def partition(self, array, left, right, pivot, cmp):
        for i in range(len(array)):
            if cmp(array[i], pivot) == 0:
                array[i], array[right] = array[right], array[i]
                break
        i = left
        temp_pivot = array[right]
        for j in range(left, right):
            if cmp(array[j], temp_pivot) == -1:
                array[i], array[j] = array[j], array[i]
                i += 1
        array[i], array[right] = array[right], array[i]
        return i
'''
使用quick sort 先对bolts 排序 用 nuts 中的一个作为pivot 进行排序
排序好了后， 再对 nuts 进行 quick sort用 bolts 进行排序
跟普通quick sort不同的是，我们需要先在原数组中 找到pivot
'''