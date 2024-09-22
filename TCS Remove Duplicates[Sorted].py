class Solution:
    def RemoveDuplicates(self,Array):
        if not Array:
            return 0
        K=1
        for i in range(1,len(Array)):
            if Array[i]!=Array[K-1]:
                Array[K]=Array[i]
                K+=1
        return K
Array = [1, 1, 2, 2, 3, 4, 4, 5]
solution=Solution()
print(solution.RemoveDuplicates(Array))