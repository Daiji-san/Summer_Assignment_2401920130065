class Solution(object):
    def longestPalindrome(self, s):
        if len(s) < 2: 
            return s
        store = [0,1]
        for i in range(len(s)):
            for l,r in ((i,i), (i, i+1)):
                while l>=0 and r < len(s) and s[l] == s[r]:
                    l-=1
                    r+=1
                if (r-(l+1)) > (store[1] - store[0]):
                    store = [l + 1, r]
        return s[store[0]:store[1]]
