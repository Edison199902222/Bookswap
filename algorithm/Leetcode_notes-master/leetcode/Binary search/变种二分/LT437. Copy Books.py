class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """

    def copyBooks(self, pages, k):
        # write your code here
        if not pages:
            return 0
        left = max(pages)
        right = sum(pages)
        while left + 1 < right:
            mid = (left + right) // 2
            if self.count(pages, mid) <= k:
                right = mid
            else:
                left = mid
        if self.count(pages, left) <= k:
            return left
        return right

    def count(self, pages, timelimit):
        time = 0
        people = 1
        for page in pages:
            if time + page > timelimit:
                time = 0
                people += 1
            time += page
        return people
'''
首先 我们写一个函数 
来判断 如果我们需要在 timelimit 这么多时间内完成所有的书， 需要几个人去操作
然后 我们用二分法 来决定要多少时间
首先 最少肯定是需要 书籍中的最大值，因为 我们假设我们有 五本书 有五个人去看 那么最少要有五本书中的最大值的时间看完
最多的话 假设我们只有一个人的话 那么就是一本一本看完 就是sum 书籍

然后我们 取mid
每次把mid 作为time limit 调用 函数， 我们可以得到 要多少人 可以在 mid 时间内完成所有书籍
如果 需要的人数 是 小于等于k的话， 说明我们的时间是多余的， 我们就可以给少一点时间 也就是right = mid 来增加k 
如果需要的人数 是大于k 的话， 说明我们不能在mid 时间内 调用k个人完成， 我们就需要给多一点时间， 来减少k
最后先检查left是不是满足条件，因为我们需要在最少的时间内完成

'''