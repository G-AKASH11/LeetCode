class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        result = 0
        vowels = {"a","e","i","o","u"}
        for i in range(left, right+1):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                result = result + 1
        return result