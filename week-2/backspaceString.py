class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        p = []
        q = []
        
        for i in range(0, len(S)):  
            if S[i] != '#':  
                q.append(S[i])  
            elif len(q) != 0:  
                q.pop()
                
        for i in range(0, len(T)):  
            if T[i] != '#':  
                p.append(T[i])  
            elif len(p) != 0:  
                p.pop()
                
        if (str(p)==str(q)):
            return True
        else:
            return False

sol = Solution()
S = "xywrrmp"
T = "xywrrmu#p"
print(sol.backspaceCompare(S,T))