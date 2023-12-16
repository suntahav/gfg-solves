#User function Template for python3

class Solution:
    def isScramble(self,S1: str, S2: str):
        ##code here
        dp = {}
        def solve(a,b):
            dpstr = a + "+"+b
            
            if dpstr in dp:
                return dp[dpstr]
            
            if len(a) != len(b):
                return False
                
            LEN = len(a)
            
            if LEN <1 :
                return False
                
            if LEN==1:
                if a==b:
                    return True
                else:
                    return False
            
            res = False
            for k in range(1, LEN):
                left = a[:k]
                right = a[k:]
                
                #No swap
                no_swap_left = solve(left, b[:k])
                no_swap_right = solve(right, b[k:])
                no_swap = no_swap_left and no_swap_right
                
                #swap
                swap_left = solve(left, b[LEN-k:])
                swap_right = solve(right, b[:LEN-k])
                swap = swap_left and swap_right
                
                res = no_swap or swap
                
                if res:
                    break
            dp[dpstr] = res
            # print(res)
            return res
            
        return solve(S1, S2)
           


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        S1,S2=input().split()
        if(Solution().isScramble( S1 , S2)):
            print("Yes")
        
        else:
            print("No")


# } Driver Code Ends