x=int(input("enter electricity unit used:"))
bill=0
if x<=100:
    bill=x*5
elif x>100 and x<200:
    bill=(100*5)+(x-100)*7
else:
    bill=(100*5)+(100*7)+(x-200)*10
print("Total Bill is :",bill)