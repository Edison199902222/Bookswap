

def height(arr):
    stack = []
    result = [-1 for i in range(len(arr))]
    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            result[stack.pop()] = i
        stack.append(i)
    return result

def main():
    list = [6,1,3,4,2,5]
    result = height(list)
    print(result)
main()
