class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # 滑动先找到当前可以满足条件的窗口
        # Once we found a window, rest part of that window will be a valid count.
        # 巧妙的就在于，其实维护了三个区间，前面跟后面一起要考虑到 避免重复
        #  xxxxc0,c1,c2 xxxx， 假设c0 c1 c2是满足条件的， 那么现在left 指向的第一个x
        # 为了避免重复以及考虑到所有情况，我们要想办法让前面的xxxx， 跟后面的 xxxx 都配上c0,c1,c2
        # 那么有几种配法呢？ 定住第一个x， 然后 用整个string 长度 减去 c2，这就是第一个可以造出这么多个substring
        # 然后移动left， 定住第二个x， 后 用整个string 长度 减去 c2， 这就是第二个x可以造出这么多个substring
        counter = collections.Counter()
        count = 0
        result = 0
        left = 0
        for right in range(len(s)):
            counter[s[right]] += 1
            if counter[s[right]] == 1:
                count += 1
            while count == 3:
                result += len(s) - right
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    count -= 1
                left += 1
        return result



