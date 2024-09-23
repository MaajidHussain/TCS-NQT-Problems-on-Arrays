class Solution:
    def SymmetricPairs(self,pairs):
        seen={}
        symmetric_pairs=[]
        
        for a,b in pairs:
            if (b,a) in seen:
                symmetric_pairs.append((b,a))
            seen[(a,b)] = True
        return symmetric_pairs
        
        
pairs= [[1,2],[2,1],[3,4],[4,5],[5,4]]
solution=Solution()
print(solution.SymmetricPairs(pairs))