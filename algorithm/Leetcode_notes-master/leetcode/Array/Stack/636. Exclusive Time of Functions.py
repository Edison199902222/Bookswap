class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # 用stack 原因是，观察所知 每个时刻我们只能处理一个任务，所以遇到end，之前的前一个任务就会结束
        # 等于stack pop掉
        stack = []
        last_time = 0
        result = [0] * n
        for i in logs:
            log = i.split(":")
            id, flag, time = int(log[0]), log[1], int(log[2])
            # 遇到start
            if flag == "start":
                # 如果前面有其他start 的话， 就要更新result了
                if stack:
                    result[stack[-1]] += time - last_time
                stack.append(id)
            else:
                # 因为 end 的话， 1 到 1 是算1 时间的
                time += 1
                # end 的话 就要把前面的程序pop出来， 因为已经结束了
                result[stack.pop()] += time - last_time
            last_time = time
        return result