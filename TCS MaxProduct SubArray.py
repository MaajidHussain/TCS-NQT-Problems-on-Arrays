class Solution:
    def maxProductSubArray(self,Array):
        prod1=Array[0]
        prod2=Array[0]
        result=Array[0]
        for i in range(1,len(Array)):
            temp=max(Array[i],prod1*Array[i],prod2*Array[i])
            prod2=min(Array[i],prod1*Array[i],prod2*Array[i])
            prod1=temp
            result=max(result,prod1)
        return result
        
Array =[2, -5, -2, -4, 3]

solution=Solution()
print(solution.maxProductSubArray(Array))