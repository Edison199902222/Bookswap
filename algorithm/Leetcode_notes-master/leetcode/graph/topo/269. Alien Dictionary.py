class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        in_degree = {x: 0 for word in words for x in word}
        neighbour = {x: [] for word in words for x in word}
        for i in range(1, len(words)):
            cur_word = words[i]
            pre_word = words[i - 1]
            for j in range(min(len(cur_word), len(pre_word))):
                if pre_word[j] == cur_word[j] and j == len(cur_word) - 1 and j != len(pre_word) - 1:
                    return ""
                if cur_word[j] != pre_word[j]:
                    in_degree[cur_word[j]] += 1
                    neighbour[pre_word[j]].append(cur_word[j])
                    break

        heap = [x for x in in_degree if in_degree[x] == 0]
        result = []
        while heap:
            word = heapq.heappop(heap)
            result.append(word)
            for node in neighbour[word]:
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    heapq.heappush(heap, node)
        return "".join(result) if len(result) == len(in_degree) else ""


'''
先用字典 构建邻居节点 与 入度
先初始化 入度 与邻居节点 
然后 遍历words 
从第二个单词开始 每次跟前一个单词比较
取他们两个的最小长度 来进行比较
注意 每次 需要检查 如果pre单词比 cur单词长 并且 到两者最小长度时 pre 跟 cur的单词字母都是一样时 
我们需要return "" 因为这是一个bad sorting 
比如 abc 跟 ab 会return ""
然后第二个需要检查的是 如果两个单词 的某个字母不相等时
那么 我们就把cur 的 字母 的入度加1
并且把pre 的字母的箭头 指向 cur 字母 
然后break

下一步 我们进行order的建立
我们利用一个heap， 把每一次入度为0 的字母 添加尽order中
然后每一次我们需要遍历当前的heap 
对于heap的每一个node来说 我们需要把它的孩子的节点 的入度 - 1 并且还需要检查
当孩子节点 -1 以后 入度为0 了 我们就要把孩子节点添加进heap之中
最后 
我们还需要检查order的数量 是不是跟degree相同 因为 有可能 如果没有入度为0的节点 就会导致添加不进order之中
'''