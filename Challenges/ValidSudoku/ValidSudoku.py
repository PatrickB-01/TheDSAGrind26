"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        og = [1,2,3,4,5,6,7,8,9]

        for i in range(9):
            #col = board[0:9][i]
            col = [r[i] for r in board]
            row = board[i]
            elesc=[]
            elesr=[]
            for j in range(9):
                if col[j] != "." and  int(col[j]) in og:
                    if int(col[j]) not in elesc:
                        elesc.append(int(col[j]))
                    else:
                        return False

                if row[j] != "." and  int(row[j]) in og:
                    if int(row[j]) not in elesr:
                        elesr.append(int(row[j]))
                    else:
                        return False
                
                if i%3 ==1 and j%3==1:
                    center = board[i][j]
                    up = board[i-1][j]
                    down = board[i+1][j]
                    left = board[i][j-1]
                    right = board[i][j+1]
                    upleft = board[i-1][j-1]
                    upright = board[i-1][j+1]
                    downleft = board[i+1][j-1]
                    downright = board[i+1][j+1]
                    quad = [center,up,down,left,right,upleft,upright,downleft,downright]
                    eleq=[]
                    for z in range(9):
                        if quad[z] != "." and  int(quad[z]) in og:
                            if int(quad[z]) not in eleq:
                                eleq.append(int(quad[z]))
                            else:
                                return False
        return True
    

    # better
    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            row = board[r]
            for c in range(9):
                v = row[c]
                if v == '.':
                    continue
                b = (r // 3) * 3 + (c // 3)
                if v in rows[r] or v in cols[c] or v in boxes[b]:
                    return False
                rows[r].add(v)
                cols[c].add(v)
                boxes[b].add(v)
        return True


s= Solution()
board = [
    [".",".","4",".",".",".","6","3","."],
    [".",".",".",".",".",".",".",".","."],
    ["5",".",".",".",".",".",".","9","."],
    [".",".",".","5","6",".",".",".","."],
    ["4",".","3",".",".",".",".",".","1"],
    [".",".",".","7",".",".",".",".","."],
    [".",".",".","5",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]
]
s.isValidSudoku(board)