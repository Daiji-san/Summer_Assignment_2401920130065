#Problem Link --> https://leetcode.com/problems/maximum-subarray/
#Description --> Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution(object):
    def maxSubArray(self, nums):
        maxSub = nums[0]
        currSum = 0

        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            maxSub = max(maxSub , currSum)
        return maxSub   
