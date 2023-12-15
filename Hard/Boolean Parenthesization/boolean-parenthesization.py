#User function Template for python3

class Solution:
    def countWays(self, N, S):
        # code here
        dp = []
        for i in range(N+1):
            temp = [[-1]*2 for j in range(N+1)]
            dp.append(temp)
                
        def solve(i, j, isTrue):
            # print(i,j, isTrue)
            if i>j:
                return 0
            
            if i==j:
                if isTrue:
                    return int(S[i] == 'T')
                else:
                    return int(S[i] == 'F')
            
            if dp[i][j][int(isTrue)] != -1:
                return dp[i][j][int(isTrue)]
            res = 0
            for k in range(i+1, j, 2):

                
                left_t = solve(i, k-1, True)
                right_t = solve(k+1, j, True)
                left_f = solve(i, k-1, False)
                right_f = solve(k+1, j, False)
                #Handle AND
                if S[k] == '&':
                    if isTrue:
                        #both should be true
                        res += (left_t * right_t)
                    else:
                        res = res+ left_f * right_f + left_t * right_f + left_f * right_t
                        
                
                #Handle OR
                elif S[k] == '|':
                    if isTrue:
                        res = res + left_t * right_t + left_t * right_f + left_f * right_t
                    else:
                        res += (left_f * right_f)
                
                #Handle XOR
                else:
                    if isTrue:
                        res = res + left_t * right_f + left_f * right_t
                    else:
                        res = res + left_f * right_f + left_t * right_t
            
                dp[i][j][int(isTrue)] = res%1003
            # print(res)
            return res%1003
        a = solve(0, N-1, True)
        return a
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        S = input()
        
        ob = Solution()
        print(ob.countWays(N, S))
# } Driver Code Ends