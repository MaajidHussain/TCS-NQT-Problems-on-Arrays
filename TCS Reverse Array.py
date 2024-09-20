class Solution:
    def ReverseArray(self,number):
        left=0
        right=len(number)-1
        while left<right:
            number[left], number[right] = number[right], number[left]
            left+=1
            right-=1
        return number
                
Array=[2,5,1,3,0]
Array1=[63,32,59,68,100,121,54,78]
Array2=[12]
solution=Solution()
print(solution.ReverseArray(Array1))