# what is the lenght of the last word in a given string
# for example: "Hellow World"  length = 5
# example 2: " my name is hawi " length = 4
# my plan is to count from the last and skip the spaces if there
# then if found a letter start counting(increament length)
# when finally see a space return the length

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) -1
        length = 0
        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length
