class Solution:
    
    def hammingWeight(self, n):
        
        count = 0
        while n != 0:
            n = n & (n - 1)
            count += 1
        return count
    
    def countBits(self, n: int) -> List[int]:
        
        ans = []
        for i in range(n + 1):
            ans.append(self.hammingWeight(i))
        return ans
    