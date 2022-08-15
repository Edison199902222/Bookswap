# The read4 API is already defined for you.
# @param buf4, List[str]
# @return an integer
# def read4(buf4):

class Solution(object):
    def __init__(self):
        self.buff = collections.deque()

    def read(self, buf, n):
        """
        :type buf: List[str]
        :type n: int
        :rtype: int
        """
        # 思路一定要清晰
        # 1. 创建 queue 作为全局中 拿着上一轮没有用完的字符
        # 2.每次read，如果queue中有字符，并且需要read，先把 上一轮没有读完的字符读
        # 3. 读完后，如果n 还是大于0，还需要读取，用buf 先读取，然后要判断 如果此时无字符可以读了，直接return
        # 4. 判断 如果读出来的数量 比我们需要的多，说明我们要把一些放进queue中暂存，需要放的字符是 总读取的数量count - 此时需要读取的数量n
        # 5.  读取 需要读取的数n 和 实际读取的数量count 的最小值， 因为有可能n 大于4 或者 count 小于 4， 取最小值不会超过4 并且也不会实际读出来的数量
        total_read = 0
        while self.buff and n > 0:
            buf[total_read] = self.buff.popleft()
            total_read += 1
            n -= 1

        while n > 0:
            buf4 = [""] * 4
            count = read4(buf4)
            # 没有数读取了
            if count == 0:
                return total_read
            # 如果读出来的数量比n大，才放进qeuue，不然就直接放进buf里面去
            if count > n:
                for i in range(count - n):
                    self.buff.append(buf4[i + n])
            for i in range(min(count, n)):
                buf[total_read] = buf4[i]
                total_read += 1
                n -= 1
        return total_read


# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.queue = collections.deque()

    def read(self, buf: List[str], n: int) -> int:
        total_read = 0
        while self.queue and n > 0:
            buf[total_read] = self.queue.popleft()
            total_read += 1
            n -= 1
        if n > 0:
            times = n // 4
            offset = n % 4
            while times > 0:
                buff = [""] * 4
                number = read4(buff)
                buf[total_read:total_read + number] = buff
                total_read += number
                times -= 1
            if offset:
                buff = [""] * 4
                number = read4(buff)
                length = min(offset, number)
                buf[total_read:total_read + length] = buff[:length]
                self.queue += buff[length:]
                total_read += length
        return total_read





