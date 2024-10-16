class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store numbers and their indices
        num_to_index = {}

        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num

            # Check if the complement is already in the dictionary
            if complement in num_to_index:
                # If found, return the indices as a list
                return [num_to_index[complement], i]

            # Otherwise, add the current number and its index to the dictionary
            num_to_index[num] = i

        # If no solution is found, return an empty list
        # (Though in this problem, it’s guaranteed to have one solution)
        return []

