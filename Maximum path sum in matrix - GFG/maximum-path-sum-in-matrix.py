#User function Template for python3

class Solution:
    def maximumPath(self, N, Matrix):
        dp = [[0] * (N + 2) for _ in range(N + 2)]
        for i in range(N):
            for j in range(N):
                dp[i + 1][j + 1] = max(dp[i][j], dp[i][j + 1], dp[i][j + 2]) + Matrix[i][j]
                
        max_sum = 0
        for i in range(len(dp)):
            for j in range(len(dp)):
                max_sum = max(max_sum, dp[i][j])
                
        return max_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.maximumPath(N, Matrix))

# } Driver Code Ends