class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #creatying a matrix of m and n grids
        self.m=len(board)
        self.n=len(board[0])
        self.word=word
        self.board=board
        
        
        #edge condition
        if len(word)>self.m *self.n:
            return False
        
        #direction array
        self.dirs=[[0,1],[-1,0],[1,0],[0,-1]]
        
        #iterate through the rows and columns of board
        for i in range(self.m):
            for j in range(self.n):
                #if the word matches the board of current row an dcolumn 
                if board[i][j]==self.word[0]:
                    #then call the dfs recursive function
                    if self.dfs(i,j,0):
                        return True
                
        #orelse return false        
        return False        
        
   #the dfs recursive function     
    def dfs(self,i,j,index):
        #action
        #if the word is found out
        if index==len(self.word):
            return True
        #changing all the values of board to hash to solvve it inplace
        if self.board[i][j]=="#":
            return False
        #traverse through the direction array
        
        self.board[i][j]=="#"
        for x,y in self.dirs:
            #nearest row and columns calculated as 
            nr=x+i
            nc=y+j
            
            #boundary check
            if nr>=0 and nr<self.m and nc>=0 and nc<self.n:
                #then increase the index by one of neighbour row an dcolumn
                self.dfs(nr,nc,index+1)
                    #if it satisfies return true
                return True
                
         #assign the board values to specific inde       
        self.board[i][j]=self.word[index]
    #or else return false    
        return False
            
            
        