from typing import List
class Solution:
    def countElements(self, arr: List[int]) -> int:
        hashset = set()
        count = 0
        for i in range(len(arr)):
            hashset.add(arr[i]+1)
        for i in range(len(arr)):
            if((arr[i]+1 in hashset) and (arr[i]+1 in arr)):
                count+=1
        return count

sol = Solution()
arr = [1,3,2,3,5,0]
print(sol.countElements(arr))