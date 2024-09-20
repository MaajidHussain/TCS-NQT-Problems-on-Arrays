class Solution:
    def freqencyElement(self,number):
        count={}
        for i in range(len(number)):
            if number[i] in count:
                count[number[i]] += 1
            else:
                count[number[i]] = 1
                
        for freq in count:
            print(freq,":",count[freq])
        
Array3=[10,5,15,10,1,15,5,10]
solution=Solution()
solution.freqencyElement(Array3)