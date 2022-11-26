#Time_Complexity: O(n)
#Space_Complexity: O(n)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #creating the list comprehension 
        board = [[False for i in range(n)] for j in range(n)]
        self.result = []
        #backtrack function 
        self.backtrack(board,0)
        #returning the resultant array
        return self.result

    #backtrack function
    def backtrack(self,board,r):
        #base condition
        if r == len(board):
            #build output string
            row = []
            #traverse through the board
            for i in range(len(board)):
                #initially string builer is empty
                stringBuilder = ""
                for j in range(len(board)):
                    #if found change it to q 
                    if board[i][j]:
                        stringBuilder+="Q"
                        #if not there change it with dot
                    else:
                        stringBuilder+="."
                        #appending the string builder to row array
                row.append(stringBuilder)
            self.result.append(row)
            return

        #traverse through the board again to find out it is safe or not
        for c in range(len(board)):
            if self.isSafe(board,r,c):
                board[r][c] = True
                #calling the backtrack function
                self.backtrack(board,r+1)

            board[r][c] = False
        #return


    #is safe function to check the queens are valid or not 
    def isSafe(self,board,i,j):
        #return type true or False
        #columns
        for r in range(0,i):
            if board[r][j]:
                return False

        r = i
        c = j
        #left diagonal
        while r>=0 and c>=0:
            if board[r][c]:
                return False
            r-=1
            c-=1

        r = i
        c = j
        #right diagonal
        while r>=0 and c<len(board):
            if board[r][c]:
                return False
            r-=1
            c+=1

        return True
        
