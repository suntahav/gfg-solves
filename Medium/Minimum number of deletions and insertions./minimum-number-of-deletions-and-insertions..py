#User function Template for python3
class Solution:
	def minOperations(self, s1, s2):
		# code here
		n = len(s1)
		m = len(s2)
		t = [[0]*(m+1) for i in range(1+n)]
		
		for i in range(1, n+1):
		    for j in range(1, m+1):
		        if s1[i-1] == s2[j-1]:
		            t[i][j] = t[i-1][j-1] + 1
		        else:
		            t[i][j] = max(t[i-1][j], t[i][j-1])
		
		return n+m-2*t[n][m]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s1,s2 = input().split()
		ob = Solution()
		ans = ob.minOperations(s1,s2)
		print(ans)
# } Driver Code Ends