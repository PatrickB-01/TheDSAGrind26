# Problem 

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

```py
def encode(self, strs: List[str]) -> str:

def decode(self, s: str) -> List[str]:
```

Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains any possible characters out of 256 valid ASCII characters.


# Attempt 1

```py
def encode(strs: list[str]) -> str:
    encoded=""
    delimiter="%$%"
    for i,s in enumerate(strs):
        if i==0 and i != len(strs)-1:
            encoded= s
        elif i!=0 :
            encoded= "".join([encoded,delimiter,s])
        elif i==0 and i == len(strs)-1:
            encoded= s
    print(encoded)
    return encoded


def decode(s: str) -> list[str]:
    decoded=""
    delimiter="%$%"
    strs=s.split(delimiter)
    return strs

```

This is actually not bad but the only problem here is that if the delimiter was not carefully chosen then it could be part of the strings.

# Solution

Although there is not specific pattern here, but encoding the strings in a way that includes the length of them helps
example:
4#Hello4#world

here the length is separated from the actual string using '#'