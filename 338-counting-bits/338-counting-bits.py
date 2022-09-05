class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            ans.append(self.hammingWeight(i))
        return ans
    
    def hammingWeight(self, num):
        count = 0
        while num != 0:
            num = num & (num - 1) 
            count += 1
        return count