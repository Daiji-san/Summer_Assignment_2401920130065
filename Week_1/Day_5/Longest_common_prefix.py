#Problem Link --> https://leetcode.com/problems/longest-common-prefix/
#Description --> Write a function to find the longest common prefix string amongst an array of strings. 
#                If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            word = strs[i]
            while word.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
