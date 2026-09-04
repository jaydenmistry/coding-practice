class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            setRow, setCol = set(), set()
            for col in range(9):
                if board[row][col] in setRow and board[row][col] != '.':
                    return False
                elif board[col][row] in setCol and board[col][row] != '.':
                    return False
                setRow.add(board[row][col])
                setCol.add(board[col][row])

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                setBox = set()
                for k in range(3):
                    for l in range(3):
                        if board[i + k][j + l] in setBox and board[i + k][j + l] != '.':
                            return False
                        setBox.add(board[i + k][j + l])
        return True
