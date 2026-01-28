"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
    // ... your code
    return encoded_string;
}
Machine 2 (receiver) has the function:

vector<string> decode(string s) {
    //... your code
    return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

Example 1:

Input: dummy_input = ["Hello","World"]

Output: ["Hello","World"]

Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
Example 2:

Input: dummy_input = [""]

Output: [""]

Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains any possible characters out of 256 valid ASCII characters.

Follow up: Could you write a generalized algorithm to work on any possible set of characters?
"""

from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        longestWord = max(strs,key=lambda w: len(w))
        position=[["_" for _ in strs] for _ in longestWord]
        header:str= "".join([str(len(longestWord)),'-',str(len(strs)),'_'])
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                position[j][i] = strs[i][j]
        
        for col in position:
            for row in col:
                header = "".join([header,row])
        return header




    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        header,body = s.split('_',1)
        longestWordSize = int(header.split('-')[0])
        numberOfStr= int(header.split('-')[1])
        strs = ["" for _ in range(numberOfStr)]
        for i in range(len(body)):
            w_pos = i % numberOfStr
            if body[i]!="_":
                strs[w_pos] = "".join([strs[w_pos],body[i]])
        return strs
    
    # Fucked up and complicated but works ^

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
    
    # concept Append "length#string" to the result.


s= Solution()
s.encode(["Hello","Word"])
s.decode(s.encode(["Hello","Word"]))