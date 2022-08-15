class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        if not slots1 or not slots2: return None
        # 先按照start 排序
        slots1 = sorted(slots1, key = lambda x : x[0])
        slots2 = sorted(slots2, key = lambda x : x[0])
        # 排序后进行比较
        i = 0
        j = 0
        m = len(slots1)
        n = len(slots2)
        while i < m and j < n:
            # 如果两个区间没有交集的话， 移动end 小的那一个，来接近另一个
            if slots1[i][0] >= slots2[j][1]:
                j += 1
            elif slots1[i][1] <= slots2[j][0]:
                i += 1
            else:
                # 如果有交集的话， 判断交集的time是不是超过了duration
                intersection_time = min(slots1[i][1], slots2[j][1]) - max(slots1[i][0], slots2[j][0])
                if intersection_time >= duration:
                    time = max(slots1[i][0], slots2[j][0])
                    return [time, time + duration]
                # 没有超过的话 继续判断移动哪个区间
                # 看end， 把end 小的 移动
                # 不能用start 进行比较
                #
                #[[0,50], [60, 70]]
                #[[10, 15], [20, 30]]
                # 8 会出错， 因为 用start 比较的话，移动的 b 下一个 有更大可能性和之前a 的毫无交集，想像包含关系的a b 数组，
                # 如果移动end比较的话， b数组的 end 的下一个的start 是最接近当前end的， 也就是 更可能和 A数组的i指针 的区间 产生交集
                if slots1[i][1] <= slots2[j][1]:
                    i += 1
                else:
                    j += 1
        return []