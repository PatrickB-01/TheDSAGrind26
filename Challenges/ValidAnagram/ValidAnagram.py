"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


"""


class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        sCounts ={}
        if len(s) != len(t):
            return False
        
        for c in s:
            if sCounts.get(c):
                sCounts[c] = sCounts[c]+1
            else:
                sCounts[c] = 1
        
        sCounts2 ={}
        for c in t:
            if sCounts.get(c):
                if sCounts2.get(c):
                    if sCounts2[c] <= sCounts[c]:
                        sCounts2[c] = sCounts2[c] + 1
                    else:
                        return False
                else:
                    sCounts2[c] = 1
            else:
                return False
        
        for k in sCounts.keys():
            if sCounts2[k] != sCounts[k]:
                return False
        return True
    
    def isAnagram2(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    def isAnagram3(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCounts ={}
        sCounts2={}
        for i in range(len(s)):
            if sCounts.get(s[i]):
                sCounts[s[i]] = sCounts[s[i]]+1
            else:
                sCounts[s[i]] = 1
            
            if sCounts2.get(t[i]):
                sCounts2[t[i]] = sCounts2[t[i]]+1
            else:
                sCounts2[t[i]] = 1
        
        if len(sCounts) != len(sCounts2):
            return False

        for k in sCounts.keys():
            if sCounts.get(k) != sCounts2.get(k):
                return False

        return True
    
    def isAnagram4(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCounts ={}
        for i in range(len(s)):
            if sCounts.get(s[i]):
                sCounts[s[i]] = sCounts[s[i]]+1
            else:
                sCounts[s[i]] = 1
        
        for i in range(len(t)):
            if sCounts.get(t[i]):
                sCounts[t[i]] = sCounts[t[i]]-1
            else:
                return False
            
        if sum(sCounts.values()) != 0:
            return False

        return True
    
    def isAnagram5(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCounts ={}
        sCounts2={}
        for i in range(len(s)):
            
            sCounts[s[i]] = sCounts.get(s[i],0)+1
            sCounts2[t[i]] = sCounts2.get(t[i],0)+1


        return sCounts2 == sCounts

        