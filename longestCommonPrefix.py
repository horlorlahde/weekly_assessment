from typing import List
class Solution(object):
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        # Iterate through the characters of the first string (strs[0]).
        for i in range(len(strs[0])):
            # For each character at position i, check if all strings have the same character at position i.
            for s in strs:
                # If a mismatch is found or if one of the strings ends, return the current result (res).
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            # If no mismatches are found, append the character to res and continue.
            res += strs[0][i] 

        return res 
              
        