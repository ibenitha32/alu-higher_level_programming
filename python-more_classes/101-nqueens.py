#!/usr/bin/python3

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set ()
        posDiag = set() # (r + c)
        negDiag = set() # (r + c)
        
        res = []
        board = [["."] * n for i in range(n)]
        
        def backtrack(r):
            if r == n:
               copy = ["".join(row) for row in board]
               res.append(copy)
                return
            for i in range(n):
                if c in col or (r + c) in posDiag or (r - c) in ned Diag:
                    continue
                    
                col.add(c)
                posDiag.add(r + c)
                nedDiag.add(r - c)
                board[r][c] = "Q"
                
                backtrack(r + 1)
                
                col.add(c)
                posDiag.add(r + c)
                nedDiag.add(r - c)
                board[r][c] = "."
           backtrack(0)
           return res
        
