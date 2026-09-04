class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        setRow, setCol = set(), set()
        for row in range(9):
            setRow.clear()
            setCol.clear()
            for col in range(9):
                if board[row][col] in setRow and board[row][col] != '.':
                    return False
                elif board[col][row] in setCol and board[col][row] != '.':
                    return False
                if board[row][col] != '.':
                    setRow.add(board[row][col])
                if board[col][row] != '.':
                    setCol.add(board[col][row])

        setBox = set()
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                setBox.clear()
                for k in range(3):
                    for l in range(3):
                        if board[i + k][j + l] in setBox and board[i + k][j + l] != '.':
                            return False
                        if board[i + k][j + l] != '.':
                            setBox.add(board[i + k][j + l])
        return True
