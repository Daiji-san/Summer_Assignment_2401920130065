#Problem Link --> https://leetcode.com/problems/ransom-note/description/

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        freq = defaultdict(int)
        for char in magazine:
            freq[char] += 1
        
        for char in ransomNote:
            if freq[char] == 0:
                return False
            freq[char] -= 1
        return True
