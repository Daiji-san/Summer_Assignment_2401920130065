class Solution(object):
    def groupAnagrams(self, strs):
        anagram = {}
        track = 0
        while track < len(strs):
            word = strs[track]
            char_f = [0]*26
            for char in word:
                index = ord(char) - 97
                char_f[index] += 1
            key = tuple(char_f)
            if key not in anagram:
                anagram[key] = [word]
            else:
                anagram[key].append(word)
            track += 1
        return list(anagram.values())
