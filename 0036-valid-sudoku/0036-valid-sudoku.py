

class Solution:
    

    def isValidSudoku(self, board):
        def three(ele,i,j,board):
            
            a = i - i%3
            b = j - j%3
            c=0
            for i in range(a,a+3):
                for j in range(b,b+3):
                    if ele==board[i][j]:
                        c+=1
            if c>1:
                        return 0
            return 1
        
        def col(ele,j,board):
            c=0
            for i in range(9):
                if board[i][j]==ele:
                    c=c+1
            if c>1:
                return 0
            return 1
            
        def row(ele,i,board):
            if board[i].count(ele)>1:
                return 0
            return 1
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                   if not(col(board[i][j],j,board)):
                       return 0
                   if not(row(board[i][j],i,board)):
                       return 0
                   if not(three(board[i][j],i,j,board)):
                       return 0
        return 1
        

