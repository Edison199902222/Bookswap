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


def main():
    list1 = [2, 1, 4, -1, 6, 1, 2, 3]
    temp = merge_list(list1, 0, len(list1) - 1)
    print(temp)
main()
