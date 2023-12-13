#User function Template for python3

class Solution:
	def LongestRepeatingSubsequence(self, a):
		# Code here
		n = len(a)
		t = [[0]*(n+1) for i in range(n+1)]
		
		for i in range(1, n+1):
		    for j in range(1, n+1):
		        if a[i-1]==a[j-1] and j!=i:
		            t[i][j] = 1+t[i-1][j-1]
		        else:
		            t[i][j]=max(t[i-1][j], t[i][j-1])
		return t[n][n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.LongestRepeatingSubsequence(str)
		print(ans)

# } Driver Code Ends