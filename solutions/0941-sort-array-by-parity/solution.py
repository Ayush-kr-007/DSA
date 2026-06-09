class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n =len(nums)
        # if nums<2:
        #     return nums
        start=0
        for i in range(n):
            if nums[i]%2==0:
                temp = nums[i]
                nums[i]=nums[start]
                nums[start]=temp
                start+=1
        return nums

