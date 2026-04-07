from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(open,close,n,temp,result):
            #base case
            if open == n and close ==n:
                result.append("".join(temp))
                return
            
            if open<n:
                temp.append('(')
                backtrack(open+1,close,n,temp,result)
                temp.pop()
            
            if close<open:
                temp.append(')')
                backtrack(open,close+1,n,temp,result)
                temp.pop()
        backtrack(0,0,n,[],result)
        return result

# Test the function
sol = Solution()
print(sol.generateParenthesis(2))

            

        