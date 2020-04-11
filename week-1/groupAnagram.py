from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        print("The original list : " + str(strs)) 
        temp = defaultdict(list) 
        print(temp)
        for ele in strs: 
	        temp[str(sorted(ele))].append(ele) 
        res = list(temp.values()) 
        print("The grouped Anagrams : " + str(res)) 
        print(temp)
        return res

sol = Solution()
arr = ['lump', 'eat', 'me', 'tea', 'em', 'plum'] 
print(sol.groupAnagrams(arr))
