class union_find:
    def __init__(self, n):
        self.father = {i: i for i in range(n)}
        self.count = {i: 1 for i in range(n)}

    def find(self, a):
        if self.father[a] == a:
            return a
        self.father[a] = self.find(self.father[a])
        return self.father[a]

    def union(self, a, b):
        father_A = self.find(a)
        father_B = self.find(b)
        if father_A != father_B:
            self.father[father_B] = father_A
            self.count[father_A] += self.count[father_B]


class Solution(object):
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        uf = union_find(n)
        primes_dic = collections.defaultdict(list)
        #  把所有拥有一样的约数的 对应在一起
        for i, num in enumerate(A):
            current_set = self.prime_set(num)
            for j in current_set:
                primes_dic[j].append(i)
        for i in primes_dic:
            for j in range(len(primes_dic[i]) - 1):
                uf.union(primes_dic[i][j], primes_dic[i][j + 1])
        return max(uf.count.values())

    def prime_set(self, n):
        out = set()
        # 如果可以除2 就除2，可以节省不必要的factor
        while n % 2 == 0:
            out.add(2)
            n //= 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                out.add(i)
                n //= i
        if n > 2:
            out.add(n)
        return out