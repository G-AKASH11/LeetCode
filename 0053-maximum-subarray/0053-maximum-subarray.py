class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=nums[0]#-2
        c=nums[0]
        for i in range(1,len(nums)):#9,
            c = max(nums[i],c+nums[i])#-2,-2+2  1,1
            m = max(c,m)#0,-2 
        return m#0