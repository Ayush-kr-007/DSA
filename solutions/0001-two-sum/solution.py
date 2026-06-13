class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        dict1={}
        for i in range(n):
            rem =target-nums[i]
            if rem in dict1:
                return [dict1[rem],i]
            
            dict1[nums[i]]=i


