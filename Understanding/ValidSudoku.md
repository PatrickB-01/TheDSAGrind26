Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.


# Attempt 1 with hint from ai

```py
def isValidSudoku(board: list[list[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = {}
    def get_boxidx(r,c) -> int:
        return (r//3)*3 + (c//3)
    
    for r in range(9):
        for c in range(9):
            value = board[r][c]
            boxidx = get_boxidx(r,c)
            if value != ".":
                if value in rows[r]:
                    return False
                else:
                    rows[r].add(value)
                if value in cols[c]:
                    return False
                else:
                    cols[c].add(value)
                
                if boxidx in boxes:
                    if value in boxes[boxidx]:
                        return False
                    else:
                        boxes[boxidx].add(value)
                else:
                    boxes[boxidx]= set()
                    boxes[boxidx].add(value)
    return True
```


Yes, you’re on the right track. The core idea is exactly to validate three independent constraints while scanning the board once: rows, columns, and 3x3 boxes. The interviewer-friendly version is: use three tracking structures and reject as soon as you see a duplicate.

The only part I’d tighten up is the box logic. Instead of trying to identify a box by its center cell, derive a stable box signature from the current cell’s indices. The standard key is:

- box row group: r // 3
- box col group: c // 3
- box index: (r // 3) * 3 + (c // 3)

So while iterating through each cell, for every non-dot value:
- check whether it already exists in that row set,
- check whether it already exists in that column set,
- check whether it already exists in that box set.

If any check fails, return false immediately. Otherwise add the value to all three sets.

One interviewer note: you do not need to separately verify that the digits are between 1 and 9, because the problem statement already guarantees that. You only need to skip dots and detect duplicates.
