class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            ans.append(self.hammingWeight(i))
        return ans
    
    def hammingWeight(self, num):
        mask = 1
        count = 0
        for i in range(32):
            if num & mask != 0:
                count += 1
            mask <<= 1
        return count