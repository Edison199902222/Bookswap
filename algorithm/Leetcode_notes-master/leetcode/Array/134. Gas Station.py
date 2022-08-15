'''
这道题
sums 记录 总共车走完全程 从第一个到最后一个 剩下多少汽油 如果大于等于0 说明肯定可以走完
current 意思是 走到第i个站 有多少汽油
如果 剩下的汽油 加上第i个站的汽油 小于下个站的汽油的话 说明走不过去了 需要跳过
'''
class Solution(object):
    def canCompleteCircuit(self,gas,cost):
        if sum(gas) - sum(cost) < 0:
            return -1
        sums,current,index = 0,0,0
        for i in range(len(gas)):
            if (current+gas[i]) < cost[i]:
                index = i+1
                current = 0
            else:
                current = current + gas[i] - cost[i]
                sums+=gas[i]-cost[i]
        if sums >= 0:
            return index
        else:
            return -1

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return - 1
        # 表示之前缺少多少油量
        lack = 0
        # 表示从index 到结尾 还剩余多少油量
        cur = 0
        index = 0
        for i in range(len(gas)):
            # 如果小于去下一站的油量，说明从起点 到 当前站 任何一个站 都不能作为起点
            # 因为如果在到当前站之前油量都大于等于0的话，那么说明他们在每个站的difference油量都是大于等于0的
            # 因为少了起点加的站的油量，到当前站肯定不可能大于等于0，
            if cur + gas[i] < cost[i]:
                lack += cur + gas[i] - cost[i]
                index = i + 1
                cur = 0
            else:
                cur += gas[i] - cost[i]
        # 如果剩余的油量，加上之前缺少的油量，都大于等于0的话，那么我们可以遍历完整个gas station
        if cur + lack >= 0:
            return index
        return - 1

if __name__ == "__main__":
    solution = Solution()
    gas = [5,1,2,3,4]
    cost = [4,4,1,5,1]
    print(solution.canCompleteCircuit(gas,cost))