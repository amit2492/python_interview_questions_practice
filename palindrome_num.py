n= int(input("Enter a number: "))
num=0
a=n
while n!=0:
    x= n%10
    num = num*10+x
    n = n//10
if a==num:
    print("Given number is palindrome")
else:
    print("Not a palindrome")