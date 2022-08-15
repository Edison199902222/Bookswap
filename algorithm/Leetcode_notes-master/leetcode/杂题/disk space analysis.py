import collections


def find_space(arr, x):
    queue = collections.deque()
    result = float("inf")
    for i in range(len(arr)):
        while queue and arr[i] < arr[queue[-1]]:
            queue.pop()
        queue.append(i)
        if i >= x - 1:
            result = min(result, arr[queue[0]])
        while i >= x - 1 and queue[0] == i - x + 1:
            queue.popleft()
    return result


def main():
    arr = [8,2,4]
    result = find_space(arr, 2)
    print(result)
main()

