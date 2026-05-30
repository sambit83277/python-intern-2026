#CHECK PASSWORD LEVEL
x=input("enter password:")
temp=0
for i in range(len(x)):
    if x[i].isdigit():
        for i in range(len(x)):
            if x[i].isupper():
                if len(x)>=8:
                   temp=1
if temp==1:
    print("password is strong")
else:
    print("password is weak")