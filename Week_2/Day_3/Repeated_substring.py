#Problem Link --> https://leetcode.com/problems/repeated-substring-pattern/

class Solution(object):
    def repeatedSubstringPattern(self, s):
        for i in range(1, len(s)//2 + 1):
            if len(s)%i == 0:
                form = s[:i]
                if form * (len(s)//i) == s:
                    return True
        return False
