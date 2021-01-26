'''
用 low 与high 代表 最少需要匹配的左括号数 和 最多需要匹配的左括号数
low 如果等于0 说明我们左括号不需要任何右括号进行匹配了
high 意思是 把所有*当成左括号
如果high 小于0 说明我们的右括号 大于 我们最多 左括号数， 说明我们右括号已经比左括号多 匹配不了了
每一次循环 我们都需要检查high 因为 ）（ 这种情况 右括号比左括号多 在左括号出现前就有 high = -1 说明不合法
然后每次 分三种情况
如果 遇到左括号 那我们 low 跟high 都需要加一
如果遇到右括号 如果low大于0 的话 我们就抵消一个 -1 如果low 不大于0， 我们此时其实把* 当作一个空
（因为有存在*号的情况 可以当作左括号 所以low可以小于0 但是我们最后要检查low是不是等于0 来判断， 因为只有等于0 才证明 左括号和右括号数量相等
 所以只能让low 保持大于等于0）
然后 high 必须要-=1
如果遇到* 那么同样 如果low 大于0的话  我们把*当成右括号 low -1
high + 1 把* 当成左括号

第二次刷的感想：
总的来说 high 保证了 右括号的总数量 是否会大于 我们最多左括号数量（把所有*当成左括号）
一旦 high保证了
那么 low表示在有左括号的情况下，将星号当作右括号时左括号的个数
而当low大于0时，说明左括号的个数太多了，没有足够多的右括号来抵消
low 保证low 不小于0 是因为 high 已经保证了  右括号的总数量 是否会大于 我们最多左括号数量
'''


class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        #最少左括号需要匹配的次数
        left_low = 0
        # 最多左括号需要匹配的次数,把所有* 当成左括号
        left_high = 0
        for i in range(len(s)):
            if s[i] == "(":
                left_low += 1
                left_high += 1
            elif s[i] == ")":
                if left_low > 0:
                    left_low -= 1
                left_high -= 1
            else:
                # 如果大于0，把 * 当成右括号
                if left_low > 0:
                    left_low -= 1
                left_high += 1
            if left_high < 0:
                return False
        return left_low == 0


class Solution:
    def checkValidString(self, s: str) -> bool:
        # 表示有最少需要匹配的左括号
        open_count = 0
        # 表示最多需要几个右括号
        need_right = 0
        for char in s:
            # 遇到左括号 open + 1
            if char == "(":
                open_count += 1
            else:
                # 遇到其他的，如果open 大于0 就减掉
                if open_count > 0:
                    open_count -= 1
            # 遇到右括号，需要的右括号就少了一个
            if char == ")":
                need_right -= 1
                # 如果最多需要的右边括号都小于0了，说明右边括号怎么样都会多于左括号，return false
                if need_right < 0:
                    return False
            else:
                # 遇到左括号 跟 星 都当成 左括号
                need_right += 1
        return open_count == 0

