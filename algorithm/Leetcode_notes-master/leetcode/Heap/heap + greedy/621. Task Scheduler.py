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
        count = collections.Counter(tasks)
        # 得到出现最多次数
        longest = max(count.values())
        word_times = 0
        # 计算有几个出现次数最多的字母
        for i in count.values():
            if i == longest:
                word_times += 1
        # 不关系怎么排列，重要的是数量最多的任务要多少个单位时间
        # （把数量最多的任务 - 1） 安排有 n 个间隔 + 最后 数量最多任务的个数
        # 特殊情况是如果 n 特别小 比如 等于= 0，
        #因为n表示相同的任务间需要间隔的个数，那么既然这里为0了，说明相同的任务可以放在一起，这里就没有任何限制了，
        #我们只需要执行完所有的任务就可以了，所以我们最终的返回结果一定不能小于任务的总个数len的，这就是要对比取较大值的原因了
        return max((longest - 1) * (n + 1) + word_times, len(tasks))

if __name__ == "__main__":
    solution = Solution()
    print(solution.leastInterval(["A","A","A","B","B"],2))


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)
        heap = []
        for key, value in count.items():
            heapq.heappush(heap, (-value, key))
        result = 0
        temp = []
        while heap or temp:
            while temp:
                heapq.heappush(heap, temp.pop())
            for i in range(max(n + 1, 1)):
                # 表示结束
                if not heap and not temp:
                    return result
                if heap:
                    frequency, word = heapq.heappop(heap)
                    result += 1
                    frequency += 1
                    if frequency < 0:
                        temp.append((frequency, word))
                else:
                    result += 1
        return result