class Solution:
    def nextGreaterElement(self, n: int) -> int:
        integer_list = [str(x) for x in str(n)]
        index = len(integer_list) - 2
        while index > -1:
            if integer_list[index] < integer_list[index + 1]:
                j = pivot = index + 1
                while j < len(integer_list) and integer_list[index] < integer_list[j]:
                    pivot = j
                    j += 1
                integer_list[index], integer_list[pivot] = integer_list[pivot], integer_list[index]
                integer_list[index + 1:] = integer_list[index + 1:][::-1]
                break
            index -= 1
        temp = int("".join(integer_list))
        return temp if temp != n and temp < 2**31 - 1 else - 1
'''
一样的套路
'''