'''
【A A A B B B] n=2
我们希望一共有k-1 个 group 然后n+1 个格子来分配
这里面 k-1 是 2 表示出现最多次数-1 n表示 间隔时间+1
我们会有 【 AB    】 【 AB   】AB 两个group
因为我们只需要将最大的那个字母 次数-1 就可以分配完成 如果最大字母都可以分配完 其他任务肯定也分配完了
然后 每个list大小 怎么去 定义呢 那肯定至少需要n个时间 才可以 A 出现在下一个group中 再加上 A，说明需要n+1时间去定义list大小
最后 我们还需要加上 最大字母，放在最后一个行。
'''

class Solution(object):
    def leastInterval(self, tasks, n):
        dic = {}
        length = len(tasks)
        for i in tasks:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        max_value = max(dic.values())
        count = 0
        for i in dic.values():
            if i == max_value:
                count+=1
        return max((max_value-1)*(n+1)+count,len(tasks))

if __name__ == "__main__":
    solution = Solution()
    print(solution.leastInterval(["A","A","A","B","B"],2))