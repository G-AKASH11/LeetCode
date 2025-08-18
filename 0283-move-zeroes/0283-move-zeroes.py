class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        non_zeroes = [num for num in nums if num!=0]
        zeroes = n-len(non_zeroes)
        result = non_zeroes + [0] *zeroes
        for i in range(n):
            nums[i]=result[i]
        return nums