#User function Template for python3

class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        t = [[-1]*(N+1) for i in range(N+1)]
        def solve(i, j):
            if i >= j:
                return 0
            if t[i][j] != -1:
                return t[i][j]
                
            res = 300000000000
            
            for k in range(i, j):
                temp = solve(i, k) + solve(k+1, j) + arr[i-1]*arr[k]*arr[j]
                if res > temp:
                    res = temp
            t[i][j] = res
            return res
        
        return solve(1, N-1)
            
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends