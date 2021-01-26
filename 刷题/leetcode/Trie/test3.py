



def make(arr):
    dic = {}
    visited = set()
    for i in range(len(arr)):
        x = arr[i][0]
        y = arr[i][1]
        if x not in dic and y not in dic:
            index = i
            while index not in visited and index + 1 not in visited:
                index += 1
            dic[x] = index
            dic[y] = index + 1
            visited.add(index)
            visited.add(index + 1)
        elif x not in dic:
            index = dic[y]
            if index - 1 not in visited:
                dic[x] = index - 1
                visited.add(index - 1)
            elif index + 1 not in visited:
                dic[x] = index + 1
                visited.add(index + 1)
        else:
            index = dic[x]
            if index - 1 not in visited:
                dic[y] = index - 1
                visited.add(index - 1)
            elif index + 1 not in visited:
                dic[y] = index + 1
                visited.add(index + 1)
    order = sorted(dic, key = lambda x:dic[x])
    result = []
    for i in order:
        result.append(i)
    return result

def main():
    list = [[3,5], [1,4], [2,4], [1,5]]
    temp = make(list)
    print(temp)
main()


