# Given

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Constraints:

m == s.length
n == t.length
1 <= m, n <= 10^5
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?


# Attempt 1

```py
def minWindow(s: str, t: str) -> str:

    freq:dict[str,int] = {}
    freq_c=[0]*(25*2)
    #65-90 A
    #97-122 a
    def fidx(c:str):
        return ord(c)-ord('A') if ord(c)<91 else 25+ ord(c)-ord('a')
    
    for c in t:
        freq[c] = freq.get(c,0) + 1
        freq_c[fidx(c)]+=1

    left=0
    right=1
    min_g=len(s)
    min_l=0
    min_r=0
    gap=0
    gap_s=0
    freq_c[fidx(s[left])] = freq_c[fidx(s[left])]- 1 if freq_c[fidx(s[left])]>0 else freq_c[fidx(s[left])]
    while right < len(s)-1 and left<=right:
        # if freq_c[fidx(s[left])]==0:
        #     left+=1
        # else:
        #     pass

        if freq_c[fidx(s[right])] > 0:
            freq_c[fidx(s[right])]-=1
            test= set(freq_c)
            if len(test)==1 and 0 in test:
                if gap<min_g:
                    min_g=gap
                    min_l=left
                    min_r=right
                
                while left < gap_s+gap+1:
                    freq_c[fidx(s[left])]+=1
                    left+=1
                    if left != right:
                        freq_c[fidx(s[left])]-=1

                gap=0
                gap_s=0
            right+=1
        elif freq_c[fidx(s[right])] == 0:
            #Extra Dup
            
        else:
            gap+=1
            if gap==1:
                gap_s=right
            right+=1

    return s[min_l:min_r+1]
```

Out of time unable to solve, hit a dead edn when i noticed that if i used the same frequency struct to shrink then i will loose the freq data


# Solution

```py
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        char_count = defaultdict(int)
        for ch in t:
            char_count[ch] += 1
        
        target_chars_remaining = len(t)
        min_window = (0, float("inf"))
        start_index = 0

        for end_index, ch in enumerate(s):
            if char_count[ch] > 0:
                target_chars_remaining -= 1
            char_count[ch] -= 1

            if target_chars_remaining == 0:
                while True:
                    char_at_start = s[start_index]
                    if char_count[char_at_start] == 0:
                        break
                    char_count[char_at_start] += 1
                    start_index += 1
                
                if end_index - start_index < min_window[1] - min_window[0]:
                    min_window = (start_index, end_index)
                
                char_count[s[start_index]] += 1
                target_chars_remaining += 1
                start_index += 1
        
        return "" if min_window[1] > len(s) else s[min_window[0]:min_window[1]+1]
```

it was better if i had continued using the hashmap  approach