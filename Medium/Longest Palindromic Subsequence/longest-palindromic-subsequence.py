#User function Template for python3

class Solution:

    def longestPalinSubseq(self, s):
        # code here
        rev = s[::-1]
        LEN = len(s)
        t = [[0]*(LEN+1) for i in range(LEN+1)]

        for i in range(1, LEN+1):
            for j in range(1, LEN+1):
                if s[i-1] == rev[j-1]:
                    t[i][j] = 1+t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        
        return t[LEN][LEN]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.longestPalinSubseq(s)
        print(ans)
# } Driver Code Ends