'''
# Brute force, works but is O(N^3)
class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    palindromes += 1
        
        return palindromes
        
'''
