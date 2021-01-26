class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        cur = []
        count = 0
        for w in words:
            # len(cur) 代表word 与word 之间的空格
            if len(cur) + count + len(w) > maxWidth:
                for i in range(maxWidth - count):
                    if len(cur) <= 1:
                        temp = 1
                    else:
                        temp = len(cur) - 1
                    cur[i % temp] += " "
                result.append("".join(cur))
                cur = []
                count = 0
            cur.append(w)
            count += len(w)
        # 使得字符串左对齐！
        result.append(" ".join(cur).ljust(maxWidth, " "))
        return result


if __name__ == '__main__':
    words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
             "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
    maxWidth = 20
    solu = Solution()

    for s in solu.fullJustify(words, maxWidth):
        print(s)
