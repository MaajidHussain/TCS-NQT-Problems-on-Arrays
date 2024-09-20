# 1st Approach without sort() takes O(n) TC. Efficient.
class Solution:
    def second_smallest_largest(self,number):
        if len(number) == 0:
            return "No Elements found in array"
        smallest=float('inf')
        second_smallest=float('inf')
        
        largest=float('-inf')
        second_largest=float('-inf')
        
        for num in number:
            if num<smallest:
                second_smallest=smallest
                smallest=num
            elif smallest<num<second_smallest:
                second_smallest=num
            
            if num>largest:
                second_largest=largest
                largest=num
            elif largest>num>second_largest:
                second_largest=num
        return second_smallest, second_largest
                
Array=[2,5,1,3,0]
Array1=[63,32,59,68,100,121,54,78]
Array2=[12]
Array3=[]
solution=Solution()
print(solution.second_smallest_largest(Array1))


# 2nd Approach using sort() which takes O(n logn) TC.
class Solution:
    def second_smallest_largest(self,number):
        number.sort()
        second_smallest=number[1]
        second_largest=number[-2]
        return second_smallest, second_largest
                
Array=[2,5,1,3,0]
Array1=[63,32,59,68,100,121,54,78]
Array2=[12]
Array3=[]
solution=Solution()
print(solution.second_smallest_largest(Array1))