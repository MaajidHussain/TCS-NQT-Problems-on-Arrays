class Solution:
    def smallestNumber(self,number):
        if len(number) == 0:
            return "No Elements found in array"
        if len(number) ==1:
            return number[0]
        small=number[0]
        for index in range(1,len(number)):
            if number[index] < big:
                small=number[index]
        return big
Array=[2,5,1,3,0]
Array1=[63,32,59,68,100,121,54,78]
Array2=[12]
Array3=[]
solution=Solution()
print(solution.smallestNumber(Array1))
