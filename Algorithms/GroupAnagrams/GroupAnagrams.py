"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""


from collections import defaultdict


class Solution:
    def isAnagram5(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCounts ={}
        sCounts2={}
        for i in range(len(s)):
            
            sCounts[s[i]] = sCounts.get(s[i],0)+1
            sCounts2[t[i]] = sCounts2.get(t[i],0)+1


        return sCounts2 == sCounts
    
    # best
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedWords={}
        for word in strs:
            sw = str(sorted(word))
            if sw in sortedWords:
                sortedWords[sw].append(word)
            else:
                sortedWords[sw]= [word]
        return list(sortedWords.values())
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams={}
        unplaced = True
        for word in strs:
            unplaced = True
            for key in anagrams.keys():
                if self.isAnagram5(word,key):
                    anagrams[key].append(word)
                    unplaced = False
                    break
            if unplaced:
                anagrams[word] = [word]
                unplaced = False
        return list(anagrams.values())


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        
        return list(ans.values())

                
