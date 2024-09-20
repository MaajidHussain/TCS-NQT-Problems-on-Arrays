# 1st approach using loop through each element in array and adding to result
class Solution:
    def ElementsSum(self,Array):
        SumTotal=0
        for element in Array:
            SumTotal+=element
        return SumTotal
        
Array3=[4,2,8,6,15,5,9,20] # Sum=69
solution=Solution()
print(solution.ElementsSum(Array3))


# 2nd Approach using sum() built-in python function
class Solution:
    def ElementsSum(self,Array):
        SumTotal=sum(Array)
        return SumTotal
        
Array3=[4,2,8,6,15,5,9,20] # Sum=69
solution=Solution()
print(solution.ElementsSum(Array3))