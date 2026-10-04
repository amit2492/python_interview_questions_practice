n = int(input("enter a number:" ))
a = n
num = 0
while n>0:
    x = n%10
    num = num*10 + x
    n = n//10

print("Reverse of the number ",+a , "is: ")
print(num)
