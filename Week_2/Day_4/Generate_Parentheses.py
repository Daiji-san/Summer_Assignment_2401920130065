class Solution(object):
    def generateParenthesis(self, n):
        result = []
        def para(curr_str, open_bracket, close_bracket):
            if len(curr_str) == 2*n:
                result.append(curr_str)
                return
            if open_bracket < n:
                para(curr_str + '(' , open_bracket + 1, close_bracket)
            if close_bracket < open_bracket:
                para(curr_str + ')', open_bracket, close_bracket + 1)
        para("", 0, 0)
        return result
