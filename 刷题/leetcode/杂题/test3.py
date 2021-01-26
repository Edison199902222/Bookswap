import collections


def bag_of_word(texts):
    hashmap = {}
    n = len(texts)
    for sentence in texts:
        cur_word = sentence.split()
        for word in cur_word:
            if word not in hashmap:
                hashmap[word] = 1
    order_word = [word for word in hashmap]
    m = len(order_word)
    order_word = sorted(order_word, key = lambda x:(str.lower(x),x))
    hashmap2 = collections.defaultdict(int)
    for i in range(len(order_word)):
        hashmap2[order_word[i]] = i
    result = [[0 for i in range(m)] for i in range(n)]
    index = 0
    for sentence in texts:
        cur_word = sentence.split()
        for word in cur_word:
            result[index][hashmap2[word]] += 1
        index += 1
    return result
if __name__ == '__main__':
    arr = ["This is an example", "that", "an example", "This is that that"]
    result = bag_of_word(arr)
    print(result)