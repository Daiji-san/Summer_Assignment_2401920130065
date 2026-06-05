#Problem Link --> https://leetcode.com/problems/valid-palindrome/
#Description --> A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
#                it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#                Given a string s, return true if it is a palindrome, or false otherwise.

class Solution(object):
    def isPalindrome(self, s):
        sentence = []
        for char in s:
            if char.isalnum():
                sentence.append(char.lower())
        final = "".join(sentence)
        return sentence == sentence[::-1]
