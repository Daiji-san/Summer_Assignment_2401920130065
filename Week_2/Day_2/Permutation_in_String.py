#Problem Link --> https://leetcode.com/problems/permutation-in-string/

class Solution(object):
    def checkInclusion(self, s1, s2):
        n1, n2 = len(s1), len(s2)
        if n1>n2:
            return False
        s1_map = {}
        window = {}
        for i in range(n1):
            s1_map[s1[i]] = s1_map.get(s1[i], 0) + 1
            window[s2[i]] = window.get(s2[i], 0) + 1
        if s1_map==window:
            return True
        for i in range(n1, n2):
            char_in = s2[i]
            char_out = s2[i-n1]
            window[char_in] = window.get(char_in, 0) + 1
            if window[char_out] == 1:
                del window[char_out]
            else:
                window[char_out] -= 1
            if s1_map == window:
                return True
        return False
