#User function Template for python3

class Solution:
    def isSubSequence(self, A, B):
        #code here
        j=0
        LEN = len(A)
        for i in range(len(B)):
            if j<LEN:
                if A[j] == B[i]:
                    # print(B[i])
                    j+=1
                else: 
                    continue
            else:
                return 1
        if j >= LEN:
            return 1
        return 0
                
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        A,B = input().split()
        ob = Solution()
        if ob.isSubSequence(A,B):
            print(1)
        else:
            print(0)

# } Driver Code Ends