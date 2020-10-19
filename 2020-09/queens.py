
class Solution:

    def totalNQueens(self, n: int) -> int:

        def isValid(row, col):
            # return board[row][col] == 0
            return not (rows[col] or hills[row - col] or dales[row + col])

        def placeQueen(row, col):
            rows[col] = 1
            hills[row - col] = 1
            dales[row + col] = 1

        def removeQueen(row, col):
            rows[col] = 0
            hills[row - col] = 0
            dales[row + col] = 0

        # def addQueen(row, col):
        #     # mark restricted areas
        #     for i in range(n):
        #         # vertical
        #         board[row][i] = 1
        #         # horizontal
        #         board[i][col] = 1
        #         # diag
        #         board[(row + i) % 8][(col + i) % 8] = 1
        #         board[(row + i) % 8][(col - i) % 8] = 1
        #     # add queen
        #     board[row][col] = 2
        #     return board

        def backtrack(row = 0, count = 0):
            print()
            for col in range(n):
                if isValid(row, col):
                    # oldBoard = board
                    placeQueen(row, col)
                    if row + 1 == n:
                        count += 1
                    else:
                        count = backtrack(row + 1, count)
                    removeQueen(row, col)
            return count


        # board = [[0] * n for _ in range(n)]
        rows = [0] * n
        hills = dales = [0] * (2 * n - 1)

        return backtrack()
# class Solution:
#     def isValid(self, row, col, board):
#         return board[row][col] == 0

#     def addQueen(self, row, col, board):
#         # mark restricted areas
#         for i in range(len(board)):
#             # vertical
#             board[row][i] = 1
#             # horizontal
#             board[i][col] = 1
#             # diag
#             board[(row + i) % 8][(col + i) % 8] = 1
#             board[(row + i) % 8][(col - i) % 8] = 1

#         # add queen
#         board[row][col] = 2
#         return board

#     def backtrack(self, row, board):
#         if row >= len(board):
#             return True

#         print(board)

#         for col in range(len(board)):
#             if self.isValid(row, col, board):
#                 newBoard = self.addQueen(row, col, board)

#                 if self.backtrack(row + 1, newBoard): return True
#         return False


#     def totalNQueens(self, n: int) -> int:
#         board = [[0] * n for _ in range(n)]

#         return self.backtrack(0, board)

print(Solution().totalNQueens(8))