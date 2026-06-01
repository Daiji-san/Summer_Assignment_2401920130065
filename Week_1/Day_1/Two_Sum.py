#Problem Link: https://leetcode.com/problems/two-sum/
#Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution(object):
    def twoSum(self, nums, target):
        num_tab = {}
        for i, num in enumerate(nums):
            second = target - num
            if second in num_tab:
                return [num_tab[second], i]
            num_tab[num] = i
