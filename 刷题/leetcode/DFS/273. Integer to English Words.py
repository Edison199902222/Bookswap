class Solution:
    def __init__(self):
        # 第一位是空是因为 让index 对应 上 数字， 1 对应 index 1
        self.lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        self.thousands = ["","Thousand","Million","Billion"]
    def numberToWords(self, num: int) -> str:
        #特殊case
        if num == 0:
            return "Zero"
        result = ""
        # 每次取最后三位 转换成english word
        for i in range(len(self.thousands)):
            # % 1000， 可以得到数字的最后三位
            if num % 1000 != 0:
                # 每次result是由 当前数字 % 1000 + 当前的千位， 加上空 再加上 之前的result
                result = self.dfs(num % 1000) + self.thousands[i] + " " + result
            num //= 1000
        # 去掉前后的空格
        return result.strip()
    def dfs(self, num):
        if num == 0:
            return ""
        # 如果小于20的话，直接return
        elif num < 20:
            return self.lessThan20[num] + " "
        # 小于100的话，从ten 里面找十位数， 然后递归个位
        elif num < 100:
            return self.tens[num // 10] + " " + self.dfs(num % 10)
        # 在二十里面找 百位的数，递归十位跟个位
        else:
            return self.lessThan20[num // 100] + " Hundred " +   self.dfs(num % 100)