class Solution:
    def find_prime(self, s):
        max_int = 10 ** 6
        current_int = int(s)
        primes = self.get_prime(min(max_int, current_int))
        n = len(s)
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i, min(i + 5, n + 1)):
                temp = int(s[i - 1: j])
                if temp < 2:
                    continue
                if primes[temp]:
                    dp[j] += dp[i - 1]
        return dp[n]

    def get_prime(self, n):
        primes = [True for i in range(n + 1)]
        primes[1] = False
        i = 2
        while i * i <= n:
            if primes[i]:  # 如果没被筛，一定是素数
                for j in range(i * i, n + 1, i):  # 筛掉它的倍数即可
                    primes[j] = False
            i += 1
        return primes


def main():
    solution = Solution()
    s = "1137"
    result = solution.find_prime(s)
    print(result)


main()
