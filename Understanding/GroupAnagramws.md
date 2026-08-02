# Problem

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

## Attempt 1

```py

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anags = []
    seen=set()
    for i,word in enumerate(strs):
        if word not in seen:
            ganags=[]
            ganags.append(word)
            
            for j,word2 in enumerate(strs):
                if i!=j and len(word2) == len(word):
                    ca={}
                    is_ana =True
                    for c in range(len(word)):
                        if word[c] in ca:
                            ca[word[c]] +=1
                        else:
                            ca[word[c]] = 1
                    for c in range(len(word)):
                        if word2[c] in ca:
                            ca[word2[c]] -= 1
                        else:
                            is_ana = False
                            break
                    
                    if is_ana:
                        for k in ca.keys():
                            if ca[k] !=0:
                                is_ana = False
                                break
                    if is_ana:
                        ganags.append(word2)
                        seen.add(word2)
            for w in ganags:
                seen.add(w)
            anags.append(ganags)
    return anags
                        
bad                   
O(n^2)

```

# Solution

what i noticed here  is that a certain signature needs to be used in order to be able to make it into O(n)
this signature can be the sorted string
```
"aet": ["eat", "tea", "ate"] 
"ant": ["tan", "nat"]
"bat": ["abt"]
```

note that the max length of a string is 100

or another signature is actually to use the fact that those are lower case english letters (26) and use the consecutive ascii values, that will lead to an array  of length 26.

once we have that signature that can be used as a key

```py
from collections import defaultdict
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    ganags = defaultdict(list)

    for s in strs:
        sig = [0]*26
        for c in s:
            index = ord(c) - ord('a')
            sig[index] +=1
        ganags[tuple(sig)].append(s)
    return list(ganags.values())
```