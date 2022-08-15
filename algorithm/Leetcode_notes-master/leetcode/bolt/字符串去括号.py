'''
-(a - b) 输出是-a + b

'''

def remove_para(string):
    result, index = dfs(0, string)
    return result



def dfs(index, string):
    cur_string = ""
    i = index
    prev_sign = "+"
    while i < len(string):
        if string[i] == "(":
            temp, i = dfs(i + 1, string)
            for j in temp:
                if j not in ["+", "-"]:
                    cur_string += j
                else:
                    if prev_sign == "-":
                        if j == "+":
                            j = "-"
                        else:
                            j = "+"
                    cur_string += j
        elif string[i] == ")":
            return cur_string, i + 1
        elif string[i] in ["+", "-"]:
            prev_sign = string[i]
            cur_string += string[i]
        else:
            cur_string += string[i]
        i += 1
    return cur_string, i

def mian():
    a = "-(a-b-c+d-(f+k))"
    result = remove_para(a)
    print(result)
mian()
