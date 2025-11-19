class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = []
        for x in nums:
            if x in visited:#1
                return x
            visited.append(x)