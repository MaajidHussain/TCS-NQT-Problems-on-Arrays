class Solution:
    def ElementsRepeating(self,Array):
        seen=set()
        repeated=set()
        for num in Array:
            if num in seen:
                repeated.add(num)
            else:
                seen.add(num)
            
        return list(repeated)
arr1 = [1,1,2,3,4,4,5,2]
solution=Solution()
print(solution.ElementsRepeating(arr1))
