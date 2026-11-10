class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for col in range(9):
            cols = set()
            for row in range(9):
                num = board[row][col]

                if num == ".":
                    continue

                if num in cols:
                    return False
                cols.add(num)
        
        for row in range(9):
            rows = set()
            for col in range(9):
                num = board[row][col]

                if num == ".":
                    continue
                
                if num in rows:
                    return False
                rows.add(num)
        
        boxes = {}

        for row in range(9):
            for col in range(9):
                num = board[row][col]

                if num == ".":
                    continue

                box_id = (row // 3) * 3 + (col // 3)

                if box_id not in boxes:
                    boxes[box_id] = set()

                if num in boxes[box_id]:
                    return False

                boxes[box_id].add(num)
        
        return True