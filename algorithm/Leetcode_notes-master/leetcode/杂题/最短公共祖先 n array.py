def lca2(root, a, b):
    if(a == root.val or b == root.val):
        return root.val

    count = 0;
    temp = None

    for child in root.children:
        res = lca2(child, a, b)
        if(res is not None):
            count += 1
            temp = res

    if(count == 2):
        return root.val

    return temp