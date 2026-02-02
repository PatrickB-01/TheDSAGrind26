"""
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""


from typing import List
from collections import OrderedDict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstring = 0
        window=[0,1]
        if len(s) ==0:
            return longestSubstring
        
        if len(s) ==1:
            return 1

        while window[1] <= len(s):
            subString = s[window[0]:window[1]]
            if subString == ''.join(OrderedDict.fromkeys(subString).keys()):
                if longestSubstring < len(subString):
                    longestSubstring = len(subString)
            else:
                window[0]+=1

            window[1]+=1
        return longestSubstring
# works but not the best

    def lengthOfLongestSubstring2(self, s: str) -> int:
        longestSubstring = left =0
        last_seen= {}
        if len(s) ==0:
            return longestSubstring
        
        for right, c in enumerate(s):
            if c in last_seen and last_seen[c] >= left:
                left = last_seen[c]+1 # this is done so that the substring is preserved without duplicate characters
            last_seen[c]=right
            longestSubstring = max(longestSubstring, right-left+1)
        return longestSubstring
# best solution

s = Solution()
string = "aua"
s.lengthOfLongestSubstring2(string)
