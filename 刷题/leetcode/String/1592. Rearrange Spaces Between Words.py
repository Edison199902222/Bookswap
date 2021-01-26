class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        space_number = len([x for x in text if x == " "])
        word = text.split()
        if len(word) == 1:
            return word[0] + " " * space_number
        space = space_number // (len(word) - 1)
        re = space_number % (len(word) - 1)
        string = ""
        for i in range(len(word) - 1):
            string += word[i] + " " * space
        return string + word[-1] + " " * re