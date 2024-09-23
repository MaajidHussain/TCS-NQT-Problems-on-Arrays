class Solution:
    def ElementsNon_Repeating(self,Array):
        count_map={}
        for num in Array:
            if num in count_map:
                count_map[num]+=
            else:
                count_map[num]=1
        nonRepeating=[num for num,count in count_map.items() if count==1]
        return nonRepeating
arr1 = [1,2,-1,1,3,1]
solution=Solution()
print(solution.ElementsNon_Repeating(arr1))
