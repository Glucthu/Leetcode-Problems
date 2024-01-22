# Problem 271 - Encode and Decode Strings
# https://leetcode.com/problems/encode-and-decode-strings

class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for word in strs:
            s += str ( len(word) ) + "#" + word

        return str(s)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            lenght = int( s[i:j] )

            strs.append(s[j+1:j+1+lenght])

            i = j+1+lenght

        return strs




