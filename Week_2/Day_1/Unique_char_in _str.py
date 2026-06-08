#Problem Link --> https://leetcode.com/problems/first-unique-character-in-a-string/description/

class Solution(object):
    def firstUniqChar(self, s):
        seen = set()
        dup = set()

        for char in s:
            if char in seen:
                dup.add(char)
            else:
                seen.add(char)
        
        for i in range(len(s)):
            if s[i] not in dup:
                return i
        return -1
