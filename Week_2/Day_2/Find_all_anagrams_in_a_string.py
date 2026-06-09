#Problem Link --> https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution(object):
    def findAnagrams(self, s, p):
        n1, n2 = len(s), len(p)
        if n2>n1:
            return []
        pcount, scount = {}, {}
        for i in range(n2):
            pcount[p[i]] = pcount.get(p[i], 0) + 1
            scount[s[i]] = scount.get(s[i], 0) + 1
        res=[0] if scount == pcount else []  
        l = 0
        for r in range(n2, n1):
            scount[s[r]] = scount.get(s[r],0) + 1
            scount[s[l]] -= 1
            if scount[s[l]] == 0:
                scount.pop(s[l])
            l+=1
            if scount == pcount:
                res.append(l)
        return res
