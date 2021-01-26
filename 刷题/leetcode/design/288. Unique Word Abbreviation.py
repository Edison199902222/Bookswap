class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.dic = collections.defaultdict(list)
        for char in dictionary:
            if len(char) <= 2:
                self.dic[char] = char
            else:
                first_letter = char[0]
                last_letter = char[-1]
                self.dic[first_letter + str(len(char) - 2) + last_letter].append(char)

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        first_letter = word[0]
        last_letter = word[-1]
        temp = first_letter + str(len(word) - 2) + last_letter
        # 要注意， 一旦call 了 self.dic[temp]， 就会创建一个对象
        if temp not in self.dic or (word in self.dic[temp] and len(self.dic[temp]) == 1):
            return True
        return False

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)