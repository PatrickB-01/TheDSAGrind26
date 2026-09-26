# Problem

Given a string s, find the length of the longest substring without duplicate characters.
Constraints:

0 <= s.length <= 10^5
s consists of English letters, digits, symbols and spaces.


# Attempt 1
```py
def lengthOfLongestSubstring(s: str) -> int:
    max_sub = 1
    start=0
    end=start+1
    subSet = set()
    subSet.add(s[start])
    while end < len(s) and start < end:
        end +=1
        if s[end-1] in subSet:
            subSet.discard(s[start])
            start += 1
            subSet.add(s[start])
            max_sub = max(max_sub,len(subSet))
        else:
            subSet.add(s[end-1])
            max_sub = max(max_sub,len(subSet))

    return max_sub
```

# Solution

```py
def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        max_sub = 1
        start=0
        end=start+1
        subSet = set()
        subSet.add(s[start])
        while end < len(s) and start < end:
            end +=1

            while s[end-1] in subSet:
                subSet.discard(s[start])
                start += 1
            
            subSet.add(s[end-1])
            max_sub = max(max_sub,len(subSet))

        return max_sub
```
I had the correct idea ,in attempt 1, of combining the set with window approach but i didn't get the logic for moving the left bound.