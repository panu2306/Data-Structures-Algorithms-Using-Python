def isValidSudoku(board):
    N = 9
    rows = [set() for _ in range(N)]
    cols = [set() for _ in range(N)]
    boxes = [set() for _ in range(N)]

    for i in range(N):
        for j in range(N):
            val = board[i][j]
            if(val == "."):
                continue
            
            # for inserting row val in elements in rows array
            if(val in rows[i]):
                return False
            rows[i].add(val)
            
            # for inserting col val in elements in cols array
            if(val in cols[j]):
                return False
            cols[j].add(val)
           
            # for inserting box elements in boxes array
            idx = (i // 3) * 3 + j // 3
            if(val in boxes[idx]):
                return False
            boxes[idx].add(val)
    return True 

# True case:
board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
"""
# False case: 
board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
"""
print("Is given sudoku a valid? ", isValidSudoku(board))
