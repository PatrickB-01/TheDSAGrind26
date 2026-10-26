# Given
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Constraints:

1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length

# Attempt 1

```py
def characterReplacement( s: str, k: int) -> int:
    left=0
    right = 1
    st = list(s)
    maxs=0
    maxs_start = left

    for i in range(len(st)):
        if st[i] == st[left]:
            right = i
            if right-left+1 > maxs:
                maxs = right-left+1
                maxs_start = left
        else:
            left= i
            right = i

    max_right = maxs_start + maxs
    changes = k
    direction = 1
    right = max_right
    left = maxs_start
    while changes != 0 and right <= len(s)-1 and left>=0:
        if direction>0:
            right += direction
            if right <= len(s)-1:
                if st[right] != st[left]:
                    changes-=1
            else:
                direction=-1
        else:
            left += direction
            if left>=0:
                if st[left]!=st[right]:
                    changes-=1

    return right-left+1

```


# Solution

```py
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = [0] * 26

        maxLen = 0
        maxFreq = 0
        left = 0
        right = 0

        while right < n:
            ch = s[right]

            freq[ord(ch) - ord('A')] += 1
            maxFreq = max(maxFreq, freq[ord(ch) - ord('A')])

            if (right - left + 1) - maxFreq > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1

            maxLen = max(maxLen, right - left + 1)
            right += 1

        return maxLen
```

# Pattern

This is a **variable-size sliding window with frequency counting**.

The window is the substring between `left` and `right`. For any window, the
best character to keep is the character that appears most often. Every other
character must be replaced, so the number of replacements needed is:

```text
window length - count of the most frequent character
```

Therefore, a window is valid when:

```text
(right - left + 1) - maxFreq <= k
```

This gives the main clue for recognizing the pattern:

> Find the longest contiguous substring that can be made uniform using at most
> `k` changes.

# How the solution works

1. Start both pointers at the beginning of the string.
2. Move `right` forward to expand the window.
3. Add the new character to `freq` and update `maxFreq`, the highest character
   frequency seen in the current or a previous window.
4. If the window needs more than `k` replacements, remove the character at
   `left` and move `left` forward.
5. Record the largest valid window length.

For example, with `s = "AABABBA"` and `k = 1`:

```text
Window  Counts        maxFreq  Replacements  Action
AA      A:2           2        0              Keep
AAB     A:2, B:1      2        1              Keep
AABA    A:3, B:1      3        1              Keep
AABAB   A:3, B:2      3        2              Shrink
```

The window `AABA` is valid because changing its one `B` to `A` makes all
characters equal. The next window would need two changes, so the left side is
advanced until the window is valid again.

# Why `maxFreq` is not decreased

When the left side moves, the frequency of a character is decreased, but
`maxFreq` is left unchanged. This is safe because `maxFreq` is only used to
find the maximum answer. A stale value can keep the window slightly larger
temporarily, but the algorithm never misses a possible maximum, and every
right pointer still moves forward only once. This preserves linear time.

# Complexity

- **Time:** `O(n)`, because each character enters and leaves the window at most
  once.
- **Space:** `O(1)`, because the frequency table has only 26 entries.