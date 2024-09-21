# 1st Approach using a for loop, which takes O(n)Time and O(1)Space
class Solution:
    def Elements_Average(self,Array):
        Size=len(Array)
        Sum=0
        for i in range(len(Array)):
            Sum+=Array[i]
        Average=Sum/Size
        if Sum%Size ==0:
            return round(Average)
        else:
            return round(Average,2)
        
Array1=[1,2,3,4,5]
Array2=[1,2,1,1,5,1]
solution=Solution()
print(solution.Elements_Average(Array1))
print(solution.Elements_Average(Array2))

# 2nd Approach using sum() biult-in function, which takes O(n)Time and O(1)Space
#and runs optimised function.
class Solution:
    def Elements_Average(self,Array):
        Size=len(Array)
        Sum=sum(Array)
        Average=Sum/Size
        if Sum%Size ==0:
            return round(Average)
        else:
            return round(Average,2)
        
Array1=[1,2,3,4,5]
Array2=[1,2,1,1,5,1]
solution=Solution()
print(solution.Elements_Average(Array1))
print(solution.Elements_Average(Array2))

