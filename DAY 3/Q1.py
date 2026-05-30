#COUNT NO OF OCCURANCE 
x=input("enter string:")
y=input("enter character:")
count=0
for i in range(len(x)):
    if x[i]==y:
        count +=1
print("The no of counts in the character is :",count)