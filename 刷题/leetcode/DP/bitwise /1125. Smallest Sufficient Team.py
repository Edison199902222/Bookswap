class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        # 把每个技能对应2进制的位数
        encode = {value: key for key, value in enumerate(req_skills)}
        # dp 中含有每一个二进制对应 最少需要的人
        dp = {0: []}
        # 遍历人，尝试把每一个人的技能跟当前dp中所有状态
        for i in range(len(people)):
            current_skill = 0
            # |取并集，表示把这个人所有技能 用二进制表示出来
            for skill in people[i]:
                current_skill |= (1 << encode[skill])

            for key, value in dp.items():
                temp = key | current_skill
                # 如果temp已经在dp出现的话，如果要更新，需要当前算的人数 比之前算的人数少
                if temp in dp and len(dp[temp]) > len(value) + 1:
                    dp[temp] = value + [i]
                elif temp not in dp:
                    dp[temp] = value + [i]

        return dp[(1 << len(req_skills)) - 1]

