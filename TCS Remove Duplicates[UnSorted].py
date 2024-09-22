class Solution:
    def removeDuplicates_Unsorted(self,Array):
        Unique=set()
        k=0
        for i in Array:
            if i not in Unique:
                Unique.add(i)
                Array[k]=i
                k+=1
        return Array[:k]
arr1 = [2, 3, 1, 9, 3, 1, 3, 9]
arr2 = [4, 3, 9, 2, 4, 1, 10, 89, 34]
solution=Solution()
print(solution.removeDuplicates_Unsorted(arr1))
print(solution.removeDuplicates_Unsorted(arr2))