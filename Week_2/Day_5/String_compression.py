class Solution(object):
    def compress(self, chars):
        write = 0
        read = 0
        while read < len(chars):
            curr_char = chars[read]
            index = 0
            while read < len(chars) and chars[read] == curr_char:
                read += 1
                index += 1
            chars[write] = curr_char
            write += 1
            if index > 1:
                for digit in str(index):
                    chars[write] = digit
                    write += 1
        return write
