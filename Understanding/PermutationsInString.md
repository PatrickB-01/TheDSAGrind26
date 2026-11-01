# Given

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.


Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:

1 <= s1.length, s2.length <= 10^4
s1 and s2 consist of lowercase English letters.

# Attempt 1


```py
def checkInclusion(s1: str, s2: str) -> bool:
    size = len(s1)
    letters = set(s1)
    left=0
    right=0
    freq = [0] * 26

    for c in s1:
        freq[ord(c) - ord('a')] += 1

    
    while right < len(s2):
        current_size = right-left+1
        if current_size < size :
            if s2[right] in letters:
                pass
            else:
                left = right+1
                right =right+1
        elif current_size == size:
            freq2 = [0] * 26
            for j in range(left,right+1):
                freq2[ord(s2[j]) - ord('a')] += 1
            if freq == freq2:
                return True
            else:
                left+=1
        right +=1

    return False
```

Cool was actually able to solve it from my first attempt , the freq idea came from previous challenges.
Also realize mid way that i need to be able to control the tail of the window so a while based on the right side is the way.
Not optimal though, but i am happy i was able to do it on my own.

# Solution

