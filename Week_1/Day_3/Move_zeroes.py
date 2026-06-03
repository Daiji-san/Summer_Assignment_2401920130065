#Problem Link --> https://leetcode.com/problems/move-zeroes/
#Description --> Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#                Note that you must do this in-place without making a copy of the array.

class Solution(object):
    def moveZeroes(self, nums):
        count = 0 #Initializes count to index 0 for tracking non zero elements
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i] #Overwrite element at nums[count]
                count += 1 
        for i in range(count, len(nums)): #This for loop changes every remaining slots(after non zero elements) to 0
            nums[i] = 0
        return nums   
