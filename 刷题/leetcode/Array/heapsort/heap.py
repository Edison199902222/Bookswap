


def shift_down(arr, index, n):
    largest = index
    max_child = 2 * index + 1
    while max_child < n:
        if max_child + 1 < n and arr[max_child + 1] > arr[max_child]:
            max_child += 1
        if arr[largest] > arr[max_child]:
            break
        arr[largest], arr[max_child] = arr[max_child], arr[largest]
        largest = max_child
        max_child = 2 * largest + 1
    return

def heap_sort(arr):
    if not arr:
        return []
    n = len(arr)
    for i in range(n // 2, -1, -1):
        shift_down(arr, i, n)
    for i in range(n - 1, 0, -1):
        # 已经做了max heap了， 首位元素是最大的， 把它放到最后一位
        arr[0], arr[i] = arr[i],arr[0]
        # 当前i 已经是前面最大值了，所以应该从0 到 i - 1做max heap
        # i - 1 的长度是 i
        shift_down(arr, 0, i)


def shift_down2(arr, index, n):
    largest = index
    min_child = 2 * index + 1
    while min_child < n:
        if min_child + 1 < n and arr[min_child + 1] < arr[min_child]:
            min_child += 1
        if arr[largest] < arr[min_child]:
            break
        arr[largest], arr[min_child] = arr[min_child], arr[largest]
        largest = min_child
        min_child = 2 * largest + 1
    return

def heap_sort2(arr):
    if not arr:
        return []
    n = len(arr)
    for i in range(n // 2, -1, -1):
        shift_down2(arr, i, n)
    for i in range(n - 1, 0, -1):
        # 已经做了max heap了， 首位元素是最大的， 把它放到最后一位
        arr[0], arr[i] = arr[i],arr[0]
        # 当前i 已经是前面最大值了，所以应该从0 到 i - 1做max heap
        # i - 1 的长度是 i
        shift_down2(arr, 0, i)


arr = [12, 11, 13, 5, 6, 7,4,3,2,5,1,6,8,2,31]
heap_sort2(arr)
print(arr)
