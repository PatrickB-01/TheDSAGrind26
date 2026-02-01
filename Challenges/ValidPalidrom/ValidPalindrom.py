"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s =  ''.join(filter(str.isalnum, s)).lower()
        isPalindrom = True
        if len(s) ==1:
            return isPalindrom
        
        for i in range(len(s)//2):
            if s[i] != s[(len(s)-1)-i]:
                return False
        
        return isPalindrom

# Two pointers from start and end iteration over half the elements but comparing all, except the mid if it's odd

s = Solution()
string = "A man, a plan, a canal: Panama"
s.isPalindrome(string)