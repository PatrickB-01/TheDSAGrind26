
# Problem

Given two strings s and t, return true if `t` is an anagram of `s`, and false otherwise.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.


# Attempts

## first

```python
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        oc= {}
        ac= {}
        for i in range(len(s)):
            if s[i] in oc:
                oc[s[i]] = oc[s[i]] + 1
            else:
                oc[s[i]] = 1
            
            if t[i] in ac:
                ac[t[i]] = ac[t[i]] + 1
            else:
                ac[t[i]] = 1
        
        for k in oc.keys():
            if k not in ac or oc[k] != ac[k]:
                return False
        return True
```

Note : space complexity here is doubled because of the use of 2 hashmaps

## second

```python
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ss = list(s)
        ss.sort()
        tt = list(t)
        tt.sort()

        return ss == tt
```

Note: this has no early stopping and is dependent of the language internals

# Solution

my first attempt was not bad but can be improved

```python
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        oc= {}
        for i in range(len(s)):
            if s[i] in oc:
                oc[s[i]]  += 1
            else:
                oc[s[i]] = 1
        
        for i in range(len(s)):    
            if t[i] in oc:
                oc[t[i]] -= 1
                if oc[t[i]] < 0:
                    return False
            else:
                return False
        
        for k in oc.keys():
            if oc[k] != 0:
                return False
        return True
```

time complexity O(n)
space complexity is O(26) because english lower case character are 26