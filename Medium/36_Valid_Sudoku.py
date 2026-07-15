from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        block = defaultdict(set)
        N = 9
        for r in range(N):
            for c in range(N):
                val = board[r][c]

                if val == '.':
                    continue

                if val in rows[r]:
                    return False
                rows[r].add(val)

                if val in cols[c]:
                    return False
                
                cols[c].add(val) 

                idx = (r//3)*3+(c//3)
                if val in block[idx]:
                    return False
                block[idx].add(val)

        return True
                
