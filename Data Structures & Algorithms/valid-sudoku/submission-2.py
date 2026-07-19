class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for i in range(9)]
        columns=[set() for i in range(9)]
        boxes=[set() for i in range(9)]

        for row in range(9):
            for column in range(9):
                value=board[row][column]
                if value==".":
                    continue
                box=(row//3)*3+(column//3)

                if value in rows[row]:
                    return False
                if value in columns[column]:
                    return False
                if value in boxes[box]:
                    return False
                rows[row].add(value)
                columns[column].add(value)
                boxes[box].add(value)  
        return True