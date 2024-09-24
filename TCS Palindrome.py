def Palindrome(Number):
    rev_number=0
    duplicate=Number
    while Number>0:
        lastDigit=Number%10
        rev_number=rev_number*10+lastDigit
        Number//=10
    return duplicate==rev_number
Number=input("Enter a number: ")
if Palindrome(Number):
    print(True)
else:
    print(False)