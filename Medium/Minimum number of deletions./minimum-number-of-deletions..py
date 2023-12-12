#User function Template for python3
class Solution:
    def minDeletions(self, s, n): 
        #code here
        rev = s[::-1]
        t = [[0]*(n+1) for i in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == rev[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        
        return n-t[n][n]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
       
        N = int(input())
        Str = input().strip()
        ob = Solution()
        ans = ob.minDeletions(Str, N)
        print(ans)
# } Driver Code Ends