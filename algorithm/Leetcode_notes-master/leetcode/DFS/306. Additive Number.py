class Solution:
    """
    @param num: a string
    @return: Is it a valid additive number
    """
    def isAdditiveNumber(self, num):
        # Write your code here
        return self.dfs(num, [])
    def dfs(self, num, path):
        if len(path) >= 3 and path[-1] != path[-2] + path[-3]:
            return False
        if not num and len(path) >= 3:
            return True
        for i in range(len(num)):
            temp = num[:i + 1]
            if (temp[0] == "0" and len(temp) != 1):
                continue
            if self.dfs(num[i + 1:], path + [int(temp)]):
                return True
        return False
'''
我们用回溯➕剪枝的方法
第一步 判断什么时候该停止
我们判断 如果path 等于3 哥或者3个以上的话 最后一个数不等于前两个数相加 那么return False
如果 num 没有数了 并且我们 path 是大于等于3 的 那么 reutrn True 因为一旦大于等于3 前面又没return False 
证明 最后一个数等于前两个数相加 而且上一层递归时也检查过 前面的数字是不是等于前两个数字相加

第二步 每一层需要干什么
在每一层递归时 我们需要遍历整个字符串num 去把他拆成有可能的数字 进行下一次递归 并且把可能的数字添加进path中， 为什么要遍历拆呢
因为 每一个数字可能是一位组成 也可能是N 多位组成 
需要判断 每一个拆出来的数字 不能以0 开头， 比如055 是无效的 但 0 可以单独作为一个
然后进行下一次递归 如果下一层递归返回的是true  那么这一层也可以返回true了
最后如果遍历完还没有返回true 那肯定就是失败了， 返回false

'''

if __name__ == "__main__":
    solution = Solution()
    print(solution.isAdditiveNumber("112358"))