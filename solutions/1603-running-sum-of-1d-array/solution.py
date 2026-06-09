class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        n = len(nums)
        res.append(nums[0])

        for i in range(1,n):
            x =  res[i-1]+nums[i]
            res.append(x)
        return res



