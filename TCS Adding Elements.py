class Solution:
    def AddingElement(self,Array):
        Array.append(6)
        Array.insert(0,7)
        Array.insert(4,8)
        return Array
arr1 = [1,2,3,4,5]
solution=Solution()
print(solution.AddingElement(arr1))
