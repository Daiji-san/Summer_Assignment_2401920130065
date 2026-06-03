#Problem Link --> https://leetcode.com/problems/squares-of-a-sorted-array/
#Description --> Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution(object):
    def sortedSquares(self, nums):
        left = 0
        right = len(nums) - 1
        result = []

        while left <= right:
            left_sq = nums[left] ** 2
            right_sq = nums[right] ** 2

            if left_sq > right_sq:
                result.append(left_sq)
                left += 1
            else:
                result.append(right_sq)
                right -= 1
        return result[::-1]
