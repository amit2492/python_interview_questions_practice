n = int(input("Enter a number: "))
if n>1: 
  for i in range(2,n):
     if n%i == 0:
        print("Given number is not a prime number")
        break
  else:
    print("Given Number is a prime ")
                
else:
    print("Provide number greater then 1 , 1 is not a prime number ")
