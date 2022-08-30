class Solution:
    def reverseBits(self, n: int) -> int:
        mask = 1
        ans = 0
        for i in range(32):
            ans *= 2
            if n & mask != 0:
                ans += 1
            mask <<= 1
        return ans
        