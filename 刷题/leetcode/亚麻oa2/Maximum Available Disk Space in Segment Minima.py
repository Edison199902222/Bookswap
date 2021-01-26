import collections


def printMaxOfMin(num_computer, arr, length):
    if len(arr) < length:
        return None
    queue = collections.deque()
    result = float("inf")
    for i in range(len(arr)):
        while queue and arr[i] < queue[-1]:
            queue.pop()
        queue.append(i)
        if i >= length - 1:
            result = min(result, arr[queue[0]])
        if queue[0] == i - length + 1:
            queue.popleft()
    return result
def main():
    lists = [8,2,4,12,5]
    result = printMaxOfMin(len(lists), lists, 2)
    print(result)
main()



