import collections


def solution(drops, dropsToOperateOn, operation):
    # Please write your code here.
    all_element = set()
    seq = []
    drops = drops.split(",")
    element_index = collections.defaultdict(int)
    index = 0
    for cur_string in drops:
        cur_seq = []
        cur = cur_string.split("->")
        for i in range(len(cur)):
            if cur[i] in all_element:
                return "INVALID"
            cur_seq.append(cur[i])
            all_element.add(cur[i])
            element_index[cur[i]] = index
        index += 1
        seq.append(cur_seq)
    if operation == "swap":
        ele = dropsToOperateOn.split(",")
        for x in ele:
            if x not in all_element:
                return "INVALID"
        index1 = element_index[ele[0]]
        index2 = element_index[ele[1]]
        final_index1 = seq[index1].index(ele[0])
        final_index2 = seq[index2].index(ele[1])
        seq[index1][final_index1], seq[index2][final_index2] = seq[index2][final_index2], seq[index1][final_index1]
    elif operation == "remove":
        ele = dropsToOperateOn
        if ele not in all_element:
            return "INVALID"
        index = element_index[ele]
        seq[index].remove(ele)
        if len(seq[index]) == 0:
            seq.pop(index)
    elif operation == "add":
        ele = dropsToOperateOn.split(",")
        add_ele1 = ele[0]
        add_ele2 = ele[1]
        if add_ele1 in all_element and add_ele2 in all_element:
            index1 = element_index[add_ele1]
            index2 = element_index[add_ele2]
            if index1 == index2:
                return "INVALID"
            final_index1 = seq[index1].index(add_ele1)
            final_index2 = seq[index2].index(add_ele2)
            removed_ele = []
            for i in range(len(seq[index2]) - 1, final_index2 - 1, - 1):
                removed_ele.append(seq[index2].pop())
            for i in range(len(removed_ele)):
                seq[index1].insert(final_index1 + 1, removed_ele.pop())
                final_index1 += 1
            if len(seq[index2]) == 0:
                seq.pop(index2)
        elif add_ele1 in all_element and add_ele2 not in all_element:
            index1 = element_index[add_ele1]
            final_index1 = seq[index1].index(add_ele1)
            seq[index1].insert(final_index1, add_ele2)
        else:
            return "INVALID"
    result = []
    for cur_seq in seq:
        if len(cur_seq) == 1:
            result.append(cur_seq[0])
        else:
            result.append("->".join(cur_seq))
    result = sorted(result, key=lambda x: len(x))
    print(result)
    return ",".join(result) if len(result) > 1 else result[0]


def main():
    result = solution("A->B->C->D,E", "A,E", "swap")
    print(result)
main()

