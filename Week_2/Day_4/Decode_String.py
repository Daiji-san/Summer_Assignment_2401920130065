class Solution(object):
    def decodeString(self, s):
        curr_k = 0
        curr_str = ""
        stack = []
        for char in s:
            if char == '[':
                stack.append((curr_str,curr_k))
                curr_str , curr_k = "", 0
            elif char == ']':
                prev_str , prev_k = stack.pop()
                curr_str = prev_str + prev_k * curr_str
            elif char.isdigit():
                curr_k = curr_k * 10 + int(char)
            else: 
                curr_str += char
        return curr_str
