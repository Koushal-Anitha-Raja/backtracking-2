class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #creating the result array
        self.result=[]
        self.backtrack(s,0,[])
        #returning the result
        return self.result
    
    def backtrack(self,s,pivot,path):
        #base condition
        if pivot ==len(s):
            #add the value to the array by shallow copying it
            self.result.append(path[:])
            return
        
        #logic
        #iterate through the string to end of string 
        for i in range(pivot,len(s)):
            #creating a substring of one character by slicing it
            substring= s[pivot:i+1]
            #to check whether the substring is palindrome or not
            if self.ispalindrome(substring):
                #action
                #if yes then append it to the path array
                path.append(substring)
                
                #recurse
                self.backtrack(s,i+1,path)
                
                #backtrack
                path.pop()
    
    #check ispalindrome or not
    def ispalindrome(self,s):
        #left pointer at start
        left=0
        #right pointer at the end
        right=len(s)-1
        #unitl the condition occurs
        while left<right:
            #if the left is equal to right then it is palindrome so increment the left and decrement the right
            if s[left]==s[right]:
                left+=1
                right-=1
                #or else return false
            else:
                return False
        return True
                
                
                
                
        
            
        