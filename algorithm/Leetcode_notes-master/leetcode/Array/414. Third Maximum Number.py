'''
先把数字 去掉重复
然后用一个长度为三数组 去维持最大的三个数 最大 第二大 第三大
然后遍历数字
如果这个数字 比 最大的都大 那么原来数组 就需要往后移动一个 第0 位变成第一位 第一位 变成第二位
如果 比第二大都大 那么第二大去替代 第三大的
'''
class Solution:
    def thirdMax(self, nums) -> int:
    	n, T = list(set(nums)), [float('-inf')]*3
    	for i in n:
    		if i > T[0]:
    			T = [i,T[0],T[1]]
    			continue
    		if i > T[1]:
    			T = [T[0],i,T[1]]
    			continue
    		if i > T[2]:
    			T = [T[0],T[1],i]
    	return T[2] if T[2] != float('-inf') else T[0]
if __name__ == "__main__":
    solution = Solution()
    print(solution.thirdMax([2,2,3,1]))