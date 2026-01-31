"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if p == "{" or p == "(" or p== "[":
                stack.append(p)
            elif len(stack) != 0:
                if p == "}" and stack[-1] == "{":
                    stack.pop()
                elif p == ")" and stack[-1] == "(":
                    stack.pop()
                elif p == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        return len(stack) == 0
    
s = Solution()
st = "(])"
s.isValid(st)