def merge_sort(A, start, end, temp):
    if start >= end:
        return
    mid = (start + end) // 2
    merge_sort(A, start, mid, temp)
    merge_sort(A, mid + 1, end, temp)
    merge(A, start, end, temp)


def merge(A, start, end, temp):
    mid = (start + end) // 2
    left = start
    right = mid + 1
    index = start
    while left <= mid and right <= end:
        if A[left] <= A[right]:
            temp[index] = A[left]
            index += 1
            left += 1
        else:
            temp[index] = A[right]
            index += 1
            right += 1
    while left <= mid:
        temp[index] = A[left]
        index += 1
        left += 1
    while right <= end:
        temp[index] = A[right]
        index += 1
        right += 1
    for i in range(start, end + 1):
        A[i] = temp[i]

def main():
    list1 = [2, 1, 4, -1, 6, 1, 2, 3]
    temp = [0] * len(list1)
    merge_sort(list1, 0, len(list1) - 1, temp)
    print(list1)
main()



def merge_list(lists, start, end):
    if start == end:
        return [lists[start]]
    mid = (start + end) // 2
    left = merge_list(lists, start, mid)
    right = merge_list(lists, mid + 1, end)
    return merge(left, right)

def merge(list1, list2):
    result = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    while i < len(list1):
        result.append(list1[i])
        i += 1
    while j < len(list2):
        result.append(list2[j])
        j += 1
    return result
