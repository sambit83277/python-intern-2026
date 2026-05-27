x=int(input("enter the year:"))
if (x%4==0 and x%100!=0):
    print("a leap year")
elif(x%400==0):
    print("not a leap year")
else:
    print("it is not a leap year")