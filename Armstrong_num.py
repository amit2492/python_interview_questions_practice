n = int(input("Enter a number: "))
num=0
a = n
while n!=0:
    x= n%10
    num = x*x*x+num
    n = n//10
if a == num :
    print("Given number is Armstrong")
else:
    print("Not an Armstrong number")
