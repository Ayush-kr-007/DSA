class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # two pointer
        left = 0
        right = len(numbers)-1

        while left<right:
            sum1 = numbers[left]+numbers[right]
            if sum1==target:
                return [left+1,right+1]
            elif sum1>target:
                right-=1
            else:
                left+=1
                

        
