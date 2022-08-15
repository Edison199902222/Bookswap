
'''
题目 给定一串字符串，切乘全部是prime number组成的
'''
class Solution:
    def find_prime(self, s):
        self.result = []
        self.dfs(0, s, [])
        return self.result

    def dfs(self, index, s, path):
        if index == len(s):
            self.result.append(path)
            return
        for i in range(index, len(s)):
            substring = s[index:i + 1]
            if self.valid((int(substring))):
                self.dfs(i + 1, s, path + [substring])
        return

    def valid(self, n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def main():
    solution = Solution()
    s = "1137"
    result = solution.find_prime(s)
    print(result)
main()