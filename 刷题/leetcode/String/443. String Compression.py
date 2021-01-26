class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        count = 1
        for i in range(len(chars)-1, - 1, -1):
            if i!= 0 and chars[i] == chars[i - 1]:
                count += 1
                chars.pop(i)
            else:
                if count > 1:
                    for item in str(count)[::-1]:
                        chars.insert(i+1,item)
                count = 1
        return len(chars)
'''
从后往前 
首先判断 i 是不是不等于 0 ，如果等于0 的话 那么我们就不能pop 因为【a】 就是【a】
并且判断 这个字符 跟前一个字符是不是相等 
如果满足的话 那么我们就可以计算 count 并且pop 当前字符出去
如果不是的话 那么 我们就判断 count 是不是大于 1 
大于1 的话 那么我们就可以 insert 我们的 count进去 
并且还要初始化count 
'''
if __name__ == "__main__":
    solution = Solution()
    print(solution.compress(["a"]))