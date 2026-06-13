class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
                
        majority_element = max(freq, key=freq.get)
        return(majority_element)
