class Solution:
    def numSquareSum(self, n: int) -> int:
        sum = 0
        while(n):
            sum += (n%10) * (n%10)
            n = int(n/10)
        return sum
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        while(1):
            slow = self.numSquareSum(slow)
            fast = self.numSquareSum(self.numSquareSum(fast))
            if(slow != fast): 
                continue; 
            else: 
                break; 
        return (slow == 1)

sol = Solution()
print(sol.isHappy(19))