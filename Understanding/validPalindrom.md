# Problem

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.

## Attempt 1

```py
def isPalindrome(s: str) -> bool:
    c = []
    for char in s:
        if char.isalnum():
            c.append(char.lower())

    if len(c) ==0:
        return True

    for i in range(len(c)//2):
        right = len(c)-i-1
        left_v = c[i]
        right_v= c[right]
        if right_v != left_v:
            return False

```

# Solution

Attempt 1 is correct but maybe  there would be a more two pointer that increment approach just to get familiar with the type of solutions

```py
def isPalindrome(s: str) -> bool:
    c = []
    for char in s:
        if char.isalnum():
            c.append(char.lower())

    if len(c) ==0:
        return True

    left = 0
    right = len(c)-1
    while left < right:
        if c[right] != c[left]:
            return False
        left +=1
        right -=1
    return True
```
just to get used to moving pointers manually based on a condition, here pointers are merging to the same index on every iteration unless the condition returns false
