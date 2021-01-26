from collections import defaultdict


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.dic = defaultdict(set)
        self.hasApple = hasApple
        for x, y in edges:
            self.dic[x].add(y)
        result, flag = self.dfs(0)
        if result != 0:
            return (result - 1) * 2
        return 0

    def dfs(self, node):
        flag = False
        sum_time = 0
        for i in self.dic[node]:
            time, is_child = self.dfs(i)
            sum_time += time
            flag = flag or is_child
        if not flag and not self.hasApple[node]:
            return sum_time, flag
        return sum_time + 1, True
'''
对于每一个node来说，result 是表示下面的有苹果的子node到父node的单向消耗的时间，
is flag是来判断自己有没有子树有苹果，所以当没有子树有苹果时，我们就需要判断我们自己是不是有苹果，
如果都没有，我们只需要返回0跟false就行，但是如果子树没有，自己有 需要返回result ➕1，这其实就是叶子结点
每次递归到叶子结点，通过叶子结点返回到上一层，来判断叶子结点到它自己父结点消耗的时间，然后父结点再返回到它自己的父结点，直到返回到root
但由于 root 如果下面有子树有苹果 或者自己有苹果的话，也会返回总的time ➕1， 但其实是不用的, 所以需要-1
'''
