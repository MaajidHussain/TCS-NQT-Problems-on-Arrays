# BruteForce Approach for Array Rotation where Time,Space Complexity are O(n)
class Solution:
    def ArrayRotation(self,Array,Swap):
        Temp=[]
        for i in range(Swap,len(Array)):
            Temp.append(Array[i])
        for j in range(Swap):
            Temp.append(Array[j])
        return Temp
        
        
Array3=[1,2,3,4,5,6,7] 
Swap=3
solution=Solution()
print(solution.ArrayRotation(Array3,Swap))
