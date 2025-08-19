class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dup = {}

        for i,num in enumerate(nums):
            if num in dup:
                if i - dup[num] <= k:
                    return True
            dup[num] = i

        return False 