#Problem Link --> https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        result = 0
        l = 0
        for r in range(len(s)):
            char = s[r]
            while char in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(char)
            size = r - l + 1
            if size > result:
                result = size
        return result
