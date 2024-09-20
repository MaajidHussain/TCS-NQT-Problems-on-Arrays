class Solution:
    def increasing_Decreasing_Order(self,Array):
        Array.sort()
        middle=len(Array)//2
        left=middle
        right=len(Array)-1
        while left<right:
            Array[left], Array[right] = Array[right], Array[left]
            left+=1
            right-=1
        return Array
Array3=[4,2,8,6,15,5,9,20]
solution=Solution()
result=solution.increasing_Decreasing_Order(Array3)
print(" ".join(map(str, result)))