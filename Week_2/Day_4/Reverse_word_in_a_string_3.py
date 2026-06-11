#Problem Link --> https://leetcode.com/problems/reverse-words-in-a-string-iii/
class Solution(object):
    def reverseWords(self, s):
        my_list = list(s)
        n = len(my_list)
        l = 0
        while l<n:
            r = l
            while r < n and my_list[r] != ' ':
                r += 1
            l_ptr, r_ptr = l, r-1
            while l_ptr < r_ptr:
                my_list[l_ptr] , my_list[r_ptr] = my_list[r_ptr], my_list[l_ptr]
                l_ptr += 1
                r_ptr -= 1
            l = r + 1
        return "".join(my_list)
