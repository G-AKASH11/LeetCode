class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count = 0
        n = len(pref)

        for word in words:
            if word[:n] == pref:
                count = count + 1
        return count
