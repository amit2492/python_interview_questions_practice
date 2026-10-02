n = int(input("Enter the number: "))

if n%100==0:
  if n%400 == 0 and n%4==0 :
    print("Given number is a Century and a leap year ")
  else:
     print("Given number is a century but not a leap year")
elif n%4==0 :
    print("Given number is a leap year but not a century")
else:
    print("Given number is not a leap year")
