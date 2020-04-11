from typing import List
class Solution:
    def maxCrossingSum(self,arr, l, m, h) : 
      
        # Include elements on left of mid. 
        sm = 0; left_sum = -10000
        
        for i in range(m, l-1, -1) : 
            sm = sm + arr[i] 
            
            if (sm > left_sum) : 
                left_sum = sm 
        
        
        # Include elements on right of mid 
        sm = 0; right_sum = -1000
        for i in range(m + 1, h + 1) : 
            sm = sm + arr[i] 
            
            if (sm > right_sum) : 
                right_sum = sm 
        
    
        # Return sum of elements on left and right of mid 
        return left_sum + right_sum

    def maxSubArraySum(self, arr, l, h):

        if (l == h) :
            return arr[l] 
  
        # Find middle point 
        m = (l + h) // 2
    
        # Return maximum of following three possible cases 
        # a) Maximum subarray sum in left half 
        # b) Maximum subarray sum in right half 
        # c) Maximum subarray sum such that the  
        #     subarray crosses the midpoint  
        return max(self.maxSubArraySum(arr, l, m), 
                self.maxSubArraySum(arr, m+1, h), 
                self.maxCrossingSum(arr, l, m, h)) 
    
    def maxSubArray(self, nums: List[int]) -> int:
        return self.maxSubArraySum(nums,0,len(nums)-1)

sol = Solution()
arr = [2, 3, 4, 5, 7]
n = len(arr)
print(sol.maxSubArray(arr))
