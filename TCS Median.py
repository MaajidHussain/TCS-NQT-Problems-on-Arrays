class Solution:
    def Median(self,Array):
        Array.sort()
        Size=len(Array)
        if Size%2 ==0:
            avg=(Array[Size//2 -1]+Array[Size//2]) /2
            return avg
        else:
            return Array[Size//2]
Array1=[4,7,1,2,5,6]
solution=Solution()
print(solution.Median(Array1))